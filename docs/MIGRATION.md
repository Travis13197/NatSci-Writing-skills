# Migration guide

## 1. Copy the skill folders

Copy the entire directories:

- skills/natsci-writing/
- skills/natsci-writing-zh/

Keep references/ and assets/ inside each skill. Do not copy only SKILL.md.

## 2. Where skills live

| Agent package | Typical skills directory |
|---|---|
| DeepSeek Harness / DSH | ~/.agents/skills/ or project .agents/skills/ |
| Codex | ~/.codex/skills/ |
| Claude Code | ~/.claude/skills/ |
| WorkBuddy / CodeBuddy and similar | the package's configured skills directory |
| Generic agent | any directory scanned for */SKILL.md |

PowerShell:

~~~powershell
$src = "C:\path\to\NatSci-Writing-skills\skills"
Copy-Item "$src\natsci-writing" "$HOME\.agents\skills\" -Recurse -Force
Copy-Item "$src\natsci-writing-zh" "$HOME\.agents\skills\" -Recurse -Force
~~~

Bash:

~~~bash
cp -R NatSci-Writing-skills/skills/natsci-writing ~/.agents/skills/
cp -R NatSci-Writing-skills/skills/natsci-writing-zh ~/.agents/skills/
~~~

Or use the installer:

~~~bash
python tools/install.py --target ~/.agents/skills --skills both --dry-run
python tools/install.py --target ~/.agents/skills --skills both
~~~

## 3. After copying

1. Restart or refresh the agent's skill catalog.
2. Confirm both skills appear with descriptions beginning "NatSci-Writing-skills".
3. Validate:
   ~~~bash
   python tools/validate_package.py --installed ~/.agents/skills
   ~~~
4. Run a smoke test in each language.

## 4. Compatibility

- Frontmatter fields: name, description, metadata.version, metadata.system, metadata.language, metadata.companion. Unknown fields are harmless.
- References use relative links; no absolute paths.
- Figure starter code requires matplotlib/pandas/numpy (Python) or ggplot2/patchwork (R), optional.
- The measured corpus statistics are documented in the skill; the corpus itself is not shipped.
- During migration the old skills nature-biology-manuscript-writing and nature-biology-manuscript-writing-zh may coexist; disable them after verifying the new ones to avoid duplicate triggers.

## 5. Rollback

Restore the previous skills directory from backup and remove the two natsci-writing folders. The installer only writes inside the target skills directory.

## 6. Migration checklist

- [ ] Both skill folders copied with references/ and assets/
- [ ] Validator passes for installed copies
- [ ] Skill catalog shows both skills
- [ ] English and Chinese smoke tests pass
- [ ] Figure demo runs and exports files
- [ ] Old duplicate skills disabled
