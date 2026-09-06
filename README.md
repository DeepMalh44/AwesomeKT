# AwesomeKT

Reusable GitHub Copilot skills and supporting tools.

## Azure Architecture Diagram Generator

The `azure-architecture-diagram-generator` skill creates and reviews editable Azure architecture diagrams in draw.io format. It requires verified Azure icons, explicit network and trust boundaries, and an Azure Cloud Adoption Framework and Well-Architected Framework review.

The skill includes:

- Guidance for overview, network, component, deployment, and flow diagrams
- Azure icon and draw.io XML conventions
- CAF and WAF review checklists
- An editable starter template
- A strict validator with regression tests

## Install for VS Code GitHub Copilot

From the repository root in PowerShell:

```powershell
$destination = "$HOME/.copilot/skills/azure-architecture-diagram-generator"
New-Item -ItemType Directory -Force -Path $destination | Out-Null
Copy-Item "azure-architecture-diagram-generator/*" $destination -Recurse -Force
```

Restart VS Code or reload the window after installation.

## Validate

Run the validator tests:

```powershell
python -m unittest discover -s azure-architecture-diagram-generator/scripts -p "test_*.py" -v
```

Validate an uncompressed draw.io file:

```powershell
python azure-architecture-diagram-generator/scripts/validate-azure-drawio.py <diagram.drawio> --strict
```
