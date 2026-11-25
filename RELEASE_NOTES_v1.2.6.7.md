# NatSci-Writing-skills 1.2.6.7

Date: 2026-11-25

This release raises the floor for evidence density and visual finish after the
PGv3 six-figure rebuild showed that panels can pass geometry, colour and text
audits while still reading as sparse.

## 1. Three evidence layers per analytical panel

Each panel must combine at least three of: individual observations, a
distribution, an estimate with interval, a reference line, an effect size, a
cross-condition contrast, or a structural annotation. The layer count is
recorded in the panel audit.

## 2. No means-only comparisons

A means-only bar chart fails. A single series must carry a confidence band,
individual points or an event rug. A two-category bar panel is acceptable only
as a control or validation panel when the same figure contains the matching
distribution.

## 3. No dimension-swap repetition

Three stacked bars that differ only by algorithm, rule and environment are a
failure; at least one variant must add a distribution, contrast or mechanism
layer so the figure reads as an argument, not a catalogue.

## 4. Visual finish

Semantic fills with an alpha hierarchy (0.15 bands, 0.55 observations, 1.0
estimates), registered colours for whiskers and edges, consistent ticks and
frames, and no mostly empty panel. A panel that only reads when enlarged fails
at the final CSS width.

## 5. Figure-level rhythm

Each row carries a distinct evidence role. Repeated encodings across a row fail
even when each panel is individually valid.
