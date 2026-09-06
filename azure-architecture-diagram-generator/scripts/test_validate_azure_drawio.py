#!/usr/bin/env python3
"""Focused tests for validate-azure-drawio.py."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate-azure-drawio.py")
SPEC = importlib.util.spec_from_file_location("validate_azure_drawio", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def diagram(component_value: str, component_style: str) -> str:
    return f"""<mxfile host="Electron">
  <diagram id="overview" name="Overview">
    <mxGraphModel><root>
      <mxCell id="0" />
      <mxCell id="1" parent="0" />
      <mxCell id="title" value="Azure Architecture" style="text;html=1;fontSize=20;" vertex="1" parent="1">
        <mxGeometry x="10" y="10" width="400" height="40" as="geometry" />
      </mxCell>
      <mxCell id="component" value="{component_value}" style="{component_style}" vertex="1" parent="1">
        <mxGeometry x="100" y="100" width="72" height="72" as="geometry" />
      </mxCell>
      <mxCell id="gaps" value="Assumptions / Design gaps: none" style="shape=note;html=1;" vertex="1" parent="1">
        <mxGeometry x="300" y="100" width="200" height="80" as="geometry" />
      </mxCell>
    </root></mxGraphModel>
  </diagram>
</mxfile>"""


def without_assumptions(xml: str) -> str:
  start = xml.index('      <mxCell id="gaps"')
  end = xml.index("      </mxCell>", start) + len("      </mxCell>\n")
  return xml[:start] + xml[end:]


class ValidatorTests(unittest.TestCase):
    def validate_xml(self, xml: str, strict: bool = True) -> tuple[list[str], list[str]]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.drawio"
            path.write_text(xml, encoding="utf-8")
            return VALIDATOR.validate(path, strict)

    def test_accepts_current_azure2_icon_with_label(self) -> None:
        errors, warnings = self.validate_xml(
            diagram(
                "Azure App Service",
                "image;aspect=fixed;html=1;image=img/lib/azure2/app_services/App_Services.svg;",
            )
        )
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_strict_mode_rejects_generic_azure_service_box(self) -> None:
        errors, _ = self.validate_xml(
            diagram("Azure App Service", "rounded=1;whiteSpace=wrap;html=1;")
        )
        self.assertTrue(any("does not use a verified Azure stencil" in error for error in errors))

    def test_rejects_unlabeled_azure_icon(self) -> None:
        errors, _ = self.validate_xml(
            diagram(
                "",
                "image;aspect=fixed;html=1;image=img/lib/azure2/networking/Load_Balancers.svg;",
            )
        )
        self.assertTrue(any("has no adjacent/product label" in error for error in errors))

    def test_strict_mode_keeps_review_advice_as_warning(self) -> None:
        errors, warnings = self.validate_xml(
            without_assumptions(
                diagram(
                    "Azure App Service",
                    "image;aspect=fixed;html=1;image=img/lib/azure2/app_services/App_Services.svg;",
                )
            )
        )
        self.assertEqual([], errors)
        self.assertTrue(any("Missing Assumptions / Design gaps note" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()