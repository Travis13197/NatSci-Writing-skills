# Architecture

## 1. System model

NatSci-Writing-skills is a two-skill system:

- natsci-writing (English)
- natsci-writing-zh (Chinese)

The skills are peers, not a parent and a translation layer. Each is self-contained: SKILL.md, references/, assets/templates/, assets/code/ and its own changelog. The only cross-link is the metadata companion field, used when a task needs the other language.

## 2. Loading model

An agent reads SKILL.md first. SKILL.md is deliberately the operating manual, not an encyclopedia:

1. It states the deliverable modes and routing.
2. It states the non-negotiable standards (argument, evidence, language, figures).
3. It names the reference files and when to read them.
4. It defines the final quality gate.

The agent then loads only the references needed for the current mode. This keeps a normal task cheap while preserving depth for manuscript, figure, revision, formatting and response work.

## 3. Layers

| Layer | Files | Purpose |
|---|---|---|
| Operating manual | SKILL.md | modes, standards, routing, release gate |
| Corpus evidence | references/journal-style-evidence.md | measured style targets, genre definitions, exemplars, limits |
| Writing diagnostics | references/writing-diagnostics.md | AI-tone and translationese lexicon, failure modes, rewrite drills |
| Editorial and innovation | references/editorial-and-submission.md; innovation-and-broad-interest.md | editorial criteria, journal fit, submission package, contribution ladder, gap engineering, broad interest |
| Main-text discipline | references/main-text-and-information-architecture.md | result classification, evidence chain, main-text/SI split, revision control |
| Statistics and integrity | references/statistics-and-reporting-integrity.md | independent unit, replication, Nature statistics, Reporting Summary, image/data integrity |
| Language and taste | references/language-and-taste.md | rhythm, voice, house style, taste diagnostics |
| Figure craft | references/figure-craft-and-information-density.md | multipanel evidence architecture, figure order, information density, vector schematics |
| Nature section craft | references/nature-section-craft.md | abstract/Introduction/Results/Discussion moves, claim escalation, audits |
| Perspective | references/perspective-and-insight.md | intellectual centre, discovery sequence, speculation, formal content |
| Perspective production | references/nature-perspective-production.md | Nature format, six-section architecture, full paragraphs, evidence hierarchy, conceptual figures, editing modes |
| Worked theory case | references/mirror-world-case-study.md | mirror-world hypothesis: six sections, Box/figures, mathematical objects, production lessons |
| Literature and citation | references/literature-search-and-citation.md | search strategy, source hierarchy, screening, synthesis, citation verification |
| AI integrity | references/ai-use-and-writing-integrity.md | authorship ban, disclosure, permitted/prohibited use, journal policy table |
| Proofreading | references/proofreading-and-polish.md | five-pass proofreading, sentence polish, grounding/rhythm, consistency |
| Production | references/manuscript-production.md | complete-manuscript pipeline, section/paper-type playbooks, journal formats, package, statements |
| Revision | references/revision-and-response.md | polishing, phrasebank, response letters, reviewer simulation |
| Figure production | references/figure-production.md | contract, archetypes, backends, design system, chart selection, QA |
| Figure standards | references/figure-standards-nature-science.md | journal specs, caption grammar, statistical display |
| Project figure overlay | figure-design-and-audit.md + panel-layout + colour audit + Baker standard + SEAL standard + R50 | author's geometry, colour, structure and release gates |
| Research design | references/research-and-language.md | topic design, hypotheses, literature synthesis |
| Data and HTML | references/html-and-data-verification.md | full-document revision, data authenticity, calculation checks |
| Project specifics | seal-project.md, translation-validation.md, dimension-annotation.md | SEAL terminology, validation, annotation |
| Prompt | references/academic-prompt-zh.md | reusable Chinese task prompt |
| Assets | assets/templates, assets/code | 17 working templates (manuscript, figure, cover letter, innovation canvas, editorial audit, reporting checklist, response, statements, AI disclosure, literature search plan, data/code/materials) and tested Python/R figure starters |

## 4. Why two language skills instead of one bilingual skill

- Chinese and English have different failure modes (translationese and 的-chains versus article use and nominalisation), different diagnostic lexicons and different delivery conventions.
- A bilingual single skill would either duplicate the same guidance twice in one file or force one language to load the other's references.
- Two peers keep each language's instructions native while allowing a task to consult the companion when a bilingual deliverable is requested.

## 5. Why monolithic SKILL.md rather than a fragment router

The predecessor nature-skills design uses a router plus many small fragments. NatSci-Writing-skills keeps a single operating manual because:

- Editors and authors need the standards visible in one pass.
- A single file is easier to audit, diff and version than a router with dozens of fragments.
- The deep material still lives in references; only the essential standards and routing stay in SKILL.md.

## 6. Assets

- Templates are Markdown working documents: manuscript outline and evidence map; figure contract; caption skeleton; response package; data/code statements; terminology ledger.
- Code starters are tested, self-contained Python and R scripts that produce a three-panel publication figure from demo data and export SVG/PDF/600-dpi raster. They encode the figure contract, one-data-plot-per-panel rule and export settings. Users replace demo data with their own CSV.

## 7. Project-specific standards

The SEAL project standards, R50 regression checklist, R50/SEAL per-panel delivery and R50-specific colour contracts are included because they are part of the author's production environment. They are labelled as project gates, not universal journal rules. Other users can ignore or replace them without touching the general writing, production or journal-figure layers.

## 8. Validation and release

- docs/COVERAGE-AUDIT.md records the layer-by-layer audit against sources.
- tools/validate_package.py checks package structure, frontmatter, skill names, versions, companion links, reference links, absolute paths, stale names, assets and required documents.
- tools/build_manifest.py regenerates manifest.json with sizes and SHA-256 checksums.
- tools/check_prose_style.py scans prose for template contrast, defensive/self-limiting language and AI vocabulary.
- tools/install.py copies skills into a target skills directory and validates the installed copies.
- CI workflow .github/workflows/validate.yml runs validation on every push and pull request.
- Releases follow semantic versioning. The system version is in VERSION and CHANGELOG.md; each skill also has its own version and changelog.

## 9. Extending the system

To add a reference:

1. Add the Markdown file under the skill's references/.
2. Add a line to the resource list in SKILL.md with when to read it.
3. Run python tools/validate_package.py --strict.
4. Update CHANGELOG.md and run python tools/build_manifest.py.

To add a language:

1. Copy the English skill directory to a new skill name.
2. Translate SKILL.md and references; keep the same relative structure.
3. Set metadata language and companion fields.
4. Update README, install.py and validator expectations.

## 10. Non-goals

- No automatic journal submission.
- No fabricated data, citations or reviewer identities.
- No redistribution of paywalled full text or private project data.
- No interactive UI; the product is the skill and its artifacts.
