# GitHub publishing checklist

## 1. Before publishing

- [ ] No private data, unpublished manuscripts, reviewer materials or paywalled full text are inside the repository. The package contains guidance and templates only.
- [ ] Confirm the license choice and update the GitHub URL in CITATION.cff. The package is source-available for non-commercial use under the NatSci-Writing-skills Non-Commercial License; adapted nature-skills portions remain Apache-2.0 and are attributed in NOTICE.md. For commercial use, a separate written license is required.
- [ ] Check author names, affiliations, contact and citation metadata.
- [ ] Run python tools/validate_package.py --strict
python tools/check_prose_style.py README.md README.zh-CN.md.
- [ ] Regenerate manifest.json: python tools/build_manifest.py.
- [ ] Test install into a temporary directory and run a smoke prompt.
- [ ] Review the English and Chinese READMEs for consistency.

## 2. Repository

Recommended name: NatSci-Writing-skills

Description: "A complete, portable agent-skill system for Nature/Science-level manuscript writing and figure production (English + Chinese)."

Topics: agent-skills, academic-writing, scientific-writing, nature, science, manuscript, figures, latex, peer-review, llm-agents.

## 3. Publish

~~~bash
git init
git add .
git commit -m "NatSci-Writing-skills v1.2.5"
git branch -M main
git remote add origin https://github.com/<user>/NatSci-Writing-skills.git
git push -u origin main
~~~

Then create a release:

- Tag: v1.2.5
- Title: NatSci-Writing-skills v1.2.5
- Attach: NatSci-Writing-skills-v1.2.5.zip (generated from the repository root)
- Release notes: copy the 1.2.5 section of CHANGELOG.md.

## 4. Post-publish checks

- [ ] README renders correctly on GitHub (English and Chinese).
- [ ] Relative links resolve (docs/, examples/, skills/).
- [ ] The CI workflow succeeds.
- [ ] The zip contains skills/, docs/, tools/, README, README.zh-CN, LICENSE, NOTICE.
- [ ] A fresh clone can run the validator and installer.
- [ ] Repository description, topics and social preview are set.

## 5. Maintenance

- Update VERSION and CHANGELOG.md for every release.
- Refresh manifest.json after content changes.
- Keep the two language skills structurally aligned; changes to shared standards should be applied to both.
- Do not accept contributions that add fabricated citations, private data or unlicensed text.

## 6. Private project material — review before public upload

The package intentionally includes the author's project-specific standards so that the production environment is complete. Before making the repository public, review these files:

- skills/natsci-writing/references/seal-project.md
- skills/natsci-writing/references/translation-validation.md
- skills/natsci-writing/references/dimension-annotation.md
- skills/natsci-writing/references/seal-supplementary-figure-standard.md
- skills/natsci-writing-zh/references/... the Chinese equivalents
- skills/natsci-writing-zh/references/figure-r50-regression-checklist.md
- project-specific passages inside figure-design-and-audit.md and SKILL.md section 9/10

Options:

1. Publish them as author-approved project documentation.
2. Move them to a private overlay and remove their entries from SKILL.md; run the validator after removal.
3. Publish a sanitized public edition and keep the full edition locally.

Never upload unpublished manuscripts, cohort tables, reviewer comments, private datasets or third-party restricted text. The corpus statistics in the skills are aggregate measures; the underlying full texts are not included.
