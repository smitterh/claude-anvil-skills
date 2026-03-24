# CLAUDE.md — claude-anvil-skills

This repo is a **living reference project** for teaching Claude how to build
Anvil Works applications. It is not a production app — it exists to generate
ground-truth `form_template.yaml` samples that feed into the `anvil-works`
Claude skill.

## Project Purpose

Each form in this project demonstrates a category of Anvil UI components,
exported as real YAML. These samples are the canonical schema reference —
more reliable than any documentation because they are direct Anvil output.

## Repo Owner
- GitHub: smitterh
- Anvil project: Claude Anvil Works Skill
- Sync: Anvil ↔ GitHub auto-sync via OAuth (not username/password)

## Current Forms

| Form | Status | Components Covered |
|------|--------|--------------------|
| `Layout_Components_Form` | ✅ Complete | ColumnPanel, GridPanel, LinearPanel, FlowPanel, XYPanel — standalone and nested |
| `Input_Components_Form` | 🔲 TODO | TextBox, TextArea, DropDown, CheckBox, RadioButton, DatePicker, FileLoader |
| `Display_Components_Form` | 🔲 TODO | Label, Button, Image, RichText, Link |
| `Data_Components_Form` | 🔲 TODO | DataGrid, DataRowPanel, RepeatingPanel, ItemTemplate |
| `Events_Form` | 🔲 TODO | event_bindings patterns, data bindings, writeback |

## How to Add a New Form

1. Open the Anvil editor for this project
2. Add a new form, drag in the target components
3. Anvil auto-pushes to GitHub
4. Run `git pull` in VS Code
5. Claude Code reads the new `form_template.yaml` and updates
   the skill's `references/form_template_components.md`

## Key Files

```
client_code/
└── Layout_Components_Form/
    ├── __init__.py             ← minimal (no logic needed for reference forms)
    └── form_template.yaml      ← the actual reference YAML

anvil.yaml                      ← app config, startup form, services
theme/                          ← default Anvil theme (do not modify)
```

## Workflow

```
Anvil editor → GitHub (auto-push) → git pull → Claude Code → git push → Anvil
```

Claude Code can read and write all files in `client_code/` and `server_code/`
and `anvil.yaml` directly. Theme files should not be modified.

## GitHub Sync Notes

- Auth method: GitHub Account (OAuth) — NOT username/password
- If sync fails with ⚠️: check GitHub Settings → Emails →
  uncheck "Block command line pushes that expose my email"
- Private repo requires Anvil Business plan or higher

## Anvil Runtime Config

- Runtime version: 3
- Client version: 3
- Python: 3.10 standard
- Legacy features: bootstrap3, class_names (required for Material Design theme)
- Startup form: Layout_Components_Form

## Claude Skill Location

The `anvil-works` skill built from this project lives in the Claude skills
library. To update it as new forms are added:

1. Claude Code reads the new `form_template.yaml`
2. Updates `references/form_template_components.md` in the skill
3. Marks the TODO checkbox for that component category as complete