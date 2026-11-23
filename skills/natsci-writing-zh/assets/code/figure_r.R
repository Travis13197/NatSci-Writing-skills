#!/usr/bin/env Rscript
# 中文说明：本脚本是 NatSci-Writing-skills 的投稿级图件起点。先写图件合同，再运行：
#   Rscript figure_r.R --demo --out ./figures
#   Rscript figure_r.R --data mydata.csv --out ./figures
# CSV 列：category,value,group（一行一个观测）。
# Publication figure starter (ggplot2 + patchwork), NatSci-Writing-skills.
#
# Workflow encoded here:
# 1. Figure contract (claim, archetype, panel map) -> CONTRACT below.
# 2. One data plot per panel; direct labels; n and uncertainty documented in the caption.
# 3. Export editable SVG/PDF plus 600-dpi TIFF/PNG; keep source data beside the figure.
#
# Usage:
#   Rscript figure_r.R --demo --out ./figures
#   Rscript figure_r.R --data mydata.csv --out ./figures
# CSV columns: category, value, group (one row per observation).

suppressPackageStartupMessages({
  library(ggplot2)
  library(patchwork)
})

CONTRACT <- list(
  core_conclusion = "Group B shifts the measured value relative to group A.",
  archetype = "quantitative grid",
  journal = "Nature (double column, 183 mm)",
  backend = "r",
  panel_map = c(a = "observation-level distribution by group",
                b = "mean difference with uncertainty",
                c = "group distributions")
)

style_theme <- function() {
  theme_classic(base_size = 7, base_family = "Arial") +
    theme(
      axis.line = element_line(linewidth = 0.4),
      axis.ticks = element_line(linewidth = 0.4),
      strip.background = element_blank(),
      legend.position = "top",
      plot.title = element_text(face = "bold", size = 8, hjust = 0)
    )
}

demo_data <- function(seed = 7) {
  set.seed(seed)
  do.call(rbind, lapply(c("A", "B"), function(g) {
    do.call(rbind, lapply(c("c1", "c2", "c3", "c4"), function(cat) {
      base <- c(c1 = 1.0, c2 = 1.4, c3 = 0.8, c4 = 1.2)[[cat]]
      shift <- ifelse(g == "B", 0.45, 0)
      data.frame(category = cat, group = g,
                 value = base + shift + rnorm(12, 0, 0.18))
    }))
  }))
}

build <- function(df, outdir) {
  dir.create(outdir, showWarnings = FALSE, recursive = TRUE)
  write.csv(df, file.path(outdir, "figure_source_data.csv"), row.names = FALSE)
  groups <- unique(df$group)

  p_a <- ggplot(df, aes(x = group, y = value)) +
    geom_jitter(width = 0.12, size = 0.9, alpha = 0.7, colour = "#132B36") +
    stat_summary(fun = median, geom = "crossbar", width = 0.5,
                 linewidth = 0.4) +
    labs(x = NULL, y = "Measured value (a.u.)", title = "a  Observations by group") +
    style_theme()

  delta <- aggregate(value ~ category, data = df[df$group == groups[1], ], FUN = mean)
  ref <- aggregate(value ~ category, data = df[df$group == groups[2], ], FUN = mean)
  d <- merge(delta, ref, by = "category", suffixes = c("_A", "_B"))
  d$diff <- d$value_B - d$value_A
  d <- d[order(d$diff), ]

  p_b <- ggplot(d, aes(x = diff, y = reorder(category, diff))) +
    geom_col(fill = "#0D5673", width = 0.6) +
    geom_vline(xintercept = 0, linetype = "dashed", linewidth = 0.4,
               colour = "#586B75") +
    labs(x = "Mean difference (B - A)", y = NULL, title = "b  Category effect") +
    style_theme()

  p_c <- ggplot(df, aes(x = group, y = value, fill = group)) +
    geom_violin(alpha = 0.45, linewidth = 0.3, colour = NA) +
    geom_jitter(width = 0.06, size = 0.5, alpha = 0.7, colour = "#132B36") +
    scale_fill_manual(values = c("#4E8EAD", "#B96359")) +
    guides(fill = "none") +
    labs(x = NULL, y = "Measured value (a.u.)", title = "c  Group distributions") +
    style_theme()

  fig <- (p_a | p_b | p_c) + plot_layout(nrow = 1)
  w <- 183 / 25.4; h <- 62 / 25.4
  base <- file.path(outdir, "figure1")

  if (requireNamespace("svglite", quietly = TRUE)) {
    svglite::svglite(paste0(base, ".svg"), width = w, height = h)
    print(fig); dev.off()
  } else {
    grDevices::svg(paste0(base, ".svg"), width = w, height = h)
    print(fig); dev.off()
  }
  grDevices::cairo_pdf(paste0(base, ".pdf"), width = w, height = h, family = "Arial")
  print(fig); dev.off()
  if (requireNamespace("ragg", quietly = TRUE)) {
    ragg::agg_tiff(paste0(base, ".tiff"), width = w, height = h, units = "in", res = 600)
    print(fig); dev.off()
  } else {
    grDevices::tiff(paste0(base, ".tiff"), width = w, height = h, units = "in", res = 600,
                    compression = "lzw")
    print(fig); dev.off()
  }
  cat("wrote", paste0(base, ".{svg,pdf,tiff}"), "\n")
  cat("contract:", CONTRACT$core_conclusion, "\n")
}

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag, default = NULL) {
  i <- match(flag, args)
  if (is.na(i) || i == length(args)) default else args[[i + 1]]
}
data_path <- get_arg("--data")
outdir <- get_arg("--out", "./figures")
df <- if (!is.null(data_path)) read.csv(data_path) else demo_data()
build(df, outdir)
