#!/usr/bin/env python3
"""Validate uncompressed Azure architecture diagrams in draw.io XML format."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


AZURE_STYLE_MARKERS = (
    "image=img/lib/azure2/",
    "mxgraph.azure.",
    "azure_public_service_icons",
    "azure-public-service-icons",
)
GENERIC_INFRASTRUCTURE_TERMS = re.compile(
    r"\b(api management|app service|application gateway|cosmos db|event hubs?|"
    r"front door|key vault|kubernetes service|load balancer|log analytics|"
    r"postgresql|service bus|sql database|storage account|virtual machines?|"
    r"virtual network|azure firewall)\b",
    re.IGNORECASE,
)
TITLE_FONT_PATTERN = re.compile(r"(?:^|;)fontSize=(\d+)(?:;|$)")


def _style_has(style: str, markers: tuple[str, ...]) -> bool:
    lowered = style.lower()
    return any(marker in lowered for marker in markers)


def _text(cell: ET.Element) -> str:
    value = cell.get("value", "")
    return re.sub(r"<[^>]+>|&#xa;|&nbsp;", " ", value).strip()


def validate(path: Path, strict: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    def quality_finding(message: str) -> None:
        (errors if strict else warnings).append(message)

    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        return [f"XML parse error: {exc}"], warnings

    mxfile = tree.getroot()
    if mxfile.tag != "mxfile":
        return [f"Root element must be <mxfile>, got <{mxfile.tag}>"], warnings

    diagrams = mxfile.findall("diagram")
    if not diagrams:
        return ["No <diagram> pages found"], warnings

    for index, diagram in enumerate(diagrams):
        page = diagram.get("name", f"page-{index + 1}")
        prefix = f"[{page}]"
        model = diagram.find("mxGraphModel")
        if model is None:
            errors.append(f"{prefix} Compressed diagrams are unsupported; save as uncompressed XML")
            continue
        root = model.find("root")
        if root is None:
            errors.append(f"{prefix} Missing <root>")
            continue

        cells = root.findall("mxCell")
        ids: dict[str, ET.Element] = {}
        for cell in cells:
            cell_id = cell.get("id")
            if not cell_id:
                errors.append(f"{prefix} Cell without id")
            elif cell_id in ids:
                errors.append(f"{prefix} Duplicate cell id '{cell_id}'")
            else:
                ids[cell_id] = cell

        if len(cells) < 2 or cells[0].get("id") != "0" or cells[1].get("id") != "1":
            errors.append(f"{prefix} Cells '0' and '1' must be first")
        if "1" not in ids or ids["1"].get("parent") != "0":
            errors.append(f"{prefix} Default layer cell '1' must have parent '0'")

        vertices = [cell for cell in cells if cell.get("vertex") == "1"]
        title_found = False
        assumptions_found = False
        azure_icon_count = 0

        for cell in cells:
            cell_id = cell.get("id", "<unknown>")
            parent = cell.get("parent")
            if cell_id != "0" and (not parent or parent not in ids):
                errors.append(f"{prefix} Cell '{cell_id}' has missing or unknown parent '{parent}'")

            style = cell.get("style", "")
            text = _text(cell)
            if cell.get("vertex") == "1":
                geometry = cell.find("mxGeometry")
                if geometry is None:
                    errors.append(f"{prefix} Vertex '{cell_id}' has no geometry")
                else:
                    try:
                        if float(geometry.get("width", "0")) <= 0 or float(geometry.get("height", "0")) <= 0:
                            errors.append(f"{prefix} Vertex '{cell_id}' must have positive width and height")
                    except ValueError:
                        errors.append(f"{prefix} Vertex '{cell_id}' has invalid dimensions")

                font_match = TITLE_FONT_PATTERN.search(style)
                if "text" in style and font_match and int(font_match.group(1)) >= 18:
                    title_found = True
                if "assumption" in text.lower() or "design gap" in text.lower():
                    assumptions_found = True

                if _style_has(style, AZURE_STYLE_MARKERS):
                    azure_icon_count += 1
                    if not text:
                        errors.append(f"{prefix} Azure icon '{cell_id}' has no adjacent/product label in its value")
                    if any(token in style for token in ("rotation=", "flipH=1", "flipV=1")):
                        errors.append(f"{prefix} Azure icon '{cell_id}' is rotated or flipped")
                    if "aspect=fixed" not in style:
                        quality_finding(f"{prefix} Azure icon '{cell_id}' should use aspect=fixed")
                elif GENERIC_INFRASTRUCTURE_TERMS.search(text):
                    message = f"{prefix} '{text}' looks like an Azure service but does not use a verified Azure stencil"
                    quality_finding(message)

            if cell.get("edge") == "1":
                source = cell.get("source")
                target = cell.get("target")
                if not source or source not in ids:
                    errors.append(f"{prefix} Edge '{cell_id}' has missing or unknown source '{source}'")
                if not target or target not in ids:
                    errors.append(f"{prefix} Edge '{cell_id}' has missing or unknown target '{target}'")

        if not title_found:
            errors.append(f"{prefix} Missing title text with fontSize 18 or larger")
        if not assumptions_found:
            warnings.append(f"{prefix} Missing Assumptions / Design gaps note")
        if azure_icon_count == 0:
            quality_finding(f"{prefix} No verified Azure stencil markers found")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("diagram", type=Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat enforceable Azure icon and service-shape findings as errors",
    )
    args = parser.parse_args()

    if not args.diagram.is_file():
        print(f"ERROR: File not found: {args.diagram}")
        return 1

    errors, warnings = validate(args.diagram, args.strict)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())