# NatSci-Writing-skills 1.2.6.8

Date: 2026-11-25

This release closes a gap exposed by a full extent audit of all 66 panels in
the PGv3 six-figure set: geometry, colour and density audits can all pass while
individual axes still hide observations.

## 1. Full data extent on both axes

Every quantitative panel must cover the current data range. Hard-coded limits
copied from earlier analyses fail, and the build computes limits from the
current table with a small margin.

## 2. Threshold views need a full-range companion

A panel that starts at a threshold (for example TM >= 0.2) either extends to
the full data range or includes a full-range companion in the same panel.

## 3. Geometry-aware audit

The panel-extent audit compares data minima and maxima with sorted limits in
value space, handling inverted axes, log axes and raster/matrix extents. It
counts explicit scatter offsets and line vertices, ignores legend proxies and
default collection offsets, and records clipped-point counts and relative
overshoot per panel.

## 4. Ticks after rescaling

Extending a limit can leave auto-locator ticks outside the view; those labels
still enter text-collision checks, so explicit in-range ticks are required.

## 5. Lessons

The PGv3 audit found stale y-limits, threshold clipping of zero-valued
endpoints, long-tailed control distributions, CI bounds beyond the mean range,
composition fractions reaching 1.0, and KDE bodies cut by the frame. These are
now part of the release regression checklist.


## 6. Visible-body and raster addendum

A first data-extent pass reported zero clipped panels while readers still saw flat violin caps, contours ending at data boundaries, markers cut on 0/1, and stale cached rasters. The gate now audits every data-artist path, extends KDE and contour grids beyond the observed range, adds marker margins, checks rendered rasters at final width, and serves versioned image URLs.
