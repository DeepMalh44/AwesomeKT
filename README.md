# AwesomeKT

Reusable agent skills and supporting tools for GitHub Copilot and Claude Code.

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

## Install for Claude Code

The skill uses the standard `SKILL.md` format, so it works in Claude Code unmodified.

### Option 1: Plugin marketplace (recommended)

```
/plugin marketplace add DeepMalh44/AwesomeKT
/plugin install azure-architecture-diagram-generator@awesomekt
```

Choose the `user` scope when prompted to make the skill available in every project.

### Option 2: Copy as a personal skill

From the repository root in PowerShell:

```powershell
$destination = "$HOME/.claude/skills/azure-architecture-diagram-generator"
New-Item -ItemType Directory -Force -Path $destination | Out-Null
Copy-Item "azure-architecture-diagram-generator/*" $destination -Recurse -Force
```

Or in bash:

```bash
mkdir -p "$HOME/.claude/skills"
cp -r azure-architecture-diagram-generator "$HOME/.claude/skills/"
```

Restart Claude Code after installation. Claude Code does not detect a skills
directory that did not exist when the session started.

### Usage

Claude invokes the skill automatically when a request matches its description, for
example "draw an Azure architecture diagram for this solution" or when editing a
`.drawio` file. You can also invoke it explicitly:

```
/azure-architecture-diagram-generator
```

Note that the frontmatter deliberately omits Claude Code's `paths` field. `paths`
restricts automatic invocation to sessions already touching matching files, which
would suppress the skill in the common case of generating a new diagram from
scratch. It is also rejected by the portable Agent Skills spec used for claude.ai
uploads.

## Validate

Run the validator tests:

```powershell
python -m unittest discover -s azure-architecture-diagram-generator/scripts -p "test_*.py" -v
```

Validate an uncompressed draw.io file:

```powershell
python azure-architecture-diagram-generator/scripts/validate-azure-drawio.py <diagram.drawio> --strict
```
