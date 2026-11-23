#!/usr/bin/env python3
"""Build or check manifest.json for NatSci-Writing-skills."""
import argparse
import hashlib
import json
import os
import sys
from datetime import date

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = [("natsci-writing", "en"), ("natsci-writing-zh", "zh")]
EXCLUDE_DIRS = {".git", "__pycache__", "_test_out", ".github_cache", ".idea", ".vscode"}
EXCLUDE_FILES = {"manifest.json"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def frontmatter_version(path):
    text = open(path, "r", encoding="utf-8").read()
    for line in text.splitlines():
        if line.strip().startswith("version:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def inventory():
    files = []
    for root, dirs, names in os.walk(PKG):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in names:
            if name in EXCLUDE_FILES or name.endswith(".zip"):
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, PKG).replace(os.sep, "/")
            files.append({"path": rel, "bytes": os.path.getsize(full), "sha256": sha256(full)})
    files.sort(key=lambda item: item["path"])
    return files


def skills_meta():
    out = []
    for name, lang in SKILLS:
        d = os.path.join(PKG, "skills", name)
        refs = len([f for f in os.listdir(os.path.join(d, "references")) if f.endswith(".md")])
        templates = len(os.listdir(os.path.join(d, "assets", "templates")))
        code = len(os.listdir(os.path.join(d, "assets", "code")))
        out.append({
            "name": name,
            "language": lang,
            "version": frontmatter_version(os.path.join(d, "SKILL.md")),
            "references": refs,
            "templates": templates,
            "code_files": code,
        })
    return out


def build():
    version = open(os.path.join(PKG, "VERSION"), encoding="utf-8").read().strip()
    files = inventory()
    return {
        "system": "NatSci-Writing-skills",
        "author": "Chuanyang Liu",
        "license": "NatSci-Writing-skills Non-Commercial License 1.0",
        "third_party": "nature-skills by Yuan Yizhe (Apache-2.0)",
        "version": version,
        "generated": date.today().isoformat(),
        "skills": skills_meta(),
        "totals": {
            "files": len(files),
            "bytes": sum(item["bytes"] for item in files),
        },
        "files": files,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit non-zero if manifest.json is stale")
    args = ap.parse_args()
    data = build()
    target = os.path.join(PKG, "manifest.json")
    if args.check:
        if not os.path.exists(target):
            print("manifest.json missing")
            return 1
        current = json.loads(open(target, encoding="utf-8").read())
        same = (current.get("version") == data["version"]
                and current.get("skills") == data["skills"]
                and current.get("files") == data["files"])
        if not same:
            print("manifest.json is stale; run python tools/build_manifest.py")
            return 1
        print("manifest.json is current")
        return 0
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("wrote manifest.json:", data["totals"]["files"], "files,", data["totals"]["bytes"], "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
