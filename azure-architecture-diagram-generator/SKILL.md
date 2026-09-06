---
name: azure-architecture-diagram-generator
description: "Use when creating, reviewing, or editing Azure architecture diagrams in draw.io (.drawio), including Azure network topology, component, deployment, data-flow, and request-flow diagrams. Requires Azure stencils and service labels, clear trust and network boundaries, and an Azure CAF/WAF-informed architecture review."
---

# Azure Architecture Diagram Generator

Create editable, uncompressed draw.io diagrams that communicate Azure design intent. Use Azure product icons for Azure resources and generic shapes only for actors, custom applications, abstract steps, notes, and boundaries.

## Workflow

1. Inspect the repository, IaC, inventory, or user-provided design before asking questions. Distinguish observed facts from assumptions.
2. Choose the smallest useful diagram set using [diagram-types.md](./references/diagram-types.md). For a nontrivial solution, prefer an overview plus focused network and flow pages over one crowded page.
3. Model subscriptions, resource groups, regions, virtual networks, subnets, trust zones, ingress, egress, private endpoints, identity, data stores, observability, and recovery paths when applicable.
4. Use draw.io's current built-in Azure library (`image=img/lib/azure2/...`) or official Azure SVG icons. Legacy `mxgraph.azure.*` stencils are acceptable when they accurately represent the service. Follow [azure-stencils.md](./references/azure-stencils.md). Never invent an icon path or shape key. If an exact icon cannot be verified, use a labeled neutral placeholder and record the gap.
5. Place the official product name adjacent to every Azure icon. Do not crop, rotate, flip, recolor, or distort official icons. Do not use an Azure product icon for a custom workload component.
6. Use containers for scope and boundaries. Keep connectors orthogonal, directional, minimally crossed, and labeled with protocol, port, or interaction when known. Mark asynchronous paths distinctly and include a legend when notation is not obvious.
   - Prefer short numbered badges and a separate flow key over sentences attached to connectors.
   - Keep connector labels to 18 characters or fewer. Put protocols, identity details, retries, and explanations in a nearby callout or step band when the label would be longer.
   - Removing connector prose must not remove dependency traceability. Associate every flow step that invokes an external service with that service using a short line, matching step number, or adjacent contract card.
   - For AI flows, identify the exact model or deployment at each invocation and show its input and output. When calls vary by mode, include a compact mode-to-call matrix.
   - Reserve clear horizontal or vertical routing corridors between rows and columns. Do not route connectors through service captions, notes, icons, or other connectors' labels.
   - Use separate text cells beneath Azure icons when the caption needs more than two short lines. Never depend on an icon cell's overflow for a service description.
7. Include a title and a compact `Assumptions / Design gaps` note. Never present inferred topology as deployed fact.
8. Review applicable CAF design areas and all five WAF pillars with [caf-waf-review.md](./references/caf-waf-review.md). This is an architecture review, not certification. Put material risks or unresolved decisions in the diagram or companion response.
9. Save as uncompressed `.drawio` XML. Start from [azure-architecture.drawio](./assets/templates/azure-architecture.drawio) or the minimal mxGraph structure in [drawio-xml.md](./references/drawio-xml.md).
10. Validate before delivery:

   ```powershell
   python "$HOME/.copilot/skills/azure-architecture-diagram-generator/scripts/validate-azure-drawio.py" <diagram.drawio> --strict
   ```

11. Open the result in VS Code with `hediet.vscode-drawio` when available. Report the generated pages, assumptions, review findings, and validation result.
12. Perform a visual readability pass at fit-to-page and 100% zoom. Check every page for text clipping, caption collisions, connector crossings, labels sitting on lines, and insufficient whitespace. Structural validation alone is not a visual review.

## Required Quality Bar

- Azure resources use verified Azure stencils or official Azure SVG assets and nearby service names.
- Diagram scope and direction are immediately clear from the title, boundaries, labels, and legend.
- Pages use a readable grid with at least 40 px between peer nodes and dedicated whitespace for connector routing. Dense content is split into another page instead of being shrunk below 11 px body text.
- Flow lines do not carry prose. Use step numbers on the diagram and explain the steps in a separate band or companion page. Connector labels, when essential, are short and have an opaque background.
- A reader can trace each step to the Azure service, model or deployment, operation, input, and output it uses without consulting source code. Conditional paths identify which modes trigger each call.
- Service captions do not overlap icons, neighboring captions, boundaries, or connectors. Two-line captions are preferred; detail belongs in callouts.
- Network diagrams show address spaces or unknown markers, subnet purpose, ingress/egress, routing/security controls, and public/private exposure.
- Component diagrams show ownership boundaries, runtime services, identity, state, dependencies, and observability.
- Flow diagrams show actors, ordered interactions, sync versus async behavior, trust transitions, failure handling, and state changes when relevant.
- High availability, scaling, backup, recovery, security, monitoring, and cost-significant choices are shown or explicitly identified as gaps.
- No unsupported claim that the design is CAF-compliant, WAF-compliant, secure, highly available, or production-ready.

## Editing Existing Diagrams

Preserve valid layout and verified icon styles. Correct structural errors and misleading notation locally. Do not replace official icons with generic rectangles merely to simplify XML. Re-run validation after every substantive edit.

When readability is the reported defect, first move prose from connectors into step-linked contract cards and separate icon captions from service details. Preserve explicit associations between each step and its dependencies. Then establish rows, columns, and routing corridors before moving individual nodes. Do not attempt to solve a crowded page only by reducing font size or adding label backgrounds.

## Sources

- [Azure architecture icons](https://learn.microsoft.com/azure/architecture/icons/)
- [Architecture design diagrams](https://learn.microsoft.com/azure/well-architected/architect-role/design-diagrams)
- [Azure Well-Architected Framework pillars](https://learn.microsoft.com/azure/well-architected/pillars)
- [Azure landing zone design areas](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/design-areas)
