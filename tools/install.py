#!/usr/bin/env python3
"""Install NatSci-Writing-skills into a target skills directory."""
import argparse
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
SKILLS = {"en": "natsci-writing", "zh": "natsci-writing-zh"}
sys.path.insert(0, HERE)
try:
    from validate_package import validate_skill
except Exception:
    validate_skill = None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True, help="target skills directory")
    ap.add_argument("--skills", default="both", choices=["both", "en", "zh"])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="overwrite existing skill directories")
    ap.add_argument("--create", action="store_true", help="create the target directory if missing")
    args = ap.parse_args()

    target = os.path.abspath(os.path.expanduser(args.target))
    if not os.path.isdir(target):
        if args.create:
            os.makedirs(target, exist_ok=True)
        else:
            print("target does not exist:", target)
            print("use --create to create it")
            return 2

    selected = list(SKILLS.values()) if args.skills == "both" else [SKILLS[args.skills]]
    failures = []
    for name in selected:
        src = os.path.join(PKG, "skills", name)
        dst = os.path.join(target, name)
        print(("would copy " if args.dry_run else "copying ") + src + " -> " + dst)
        if args.dry_run:
            continue
        if os.path.exists(dst):
            if not args.force:
                print("  exists; use --force to overwrite")
                failures.append(name)
                continue
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        if validate_skill:
            errors, warnings = validate_skill(dst, name, "en" if name == "natsci-writing" else "zh")
            if errors:
                failures.append(name)
                for item in errors:
                    print("  ERROR:", item)
            else:
                print("  validated")
    if args.dry_run:
        print("dry run complete")
        return 0
    print("installed:", ", ".join(selected))
    print("next: refresh the agent skill catalog and run a smoke prompt; see docs/MIGRATION.md")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
