import argparse
import os
import re
import shutil
import zipfile
from pathlib import Path


def add_tree(archive: zipfile.ZipFile, source: Path, arc_root: Path = Path(".")) -> None:
    for path in source.rglob("*"):
        if path.is_file():
            archive.write(path, (arc_root / path.relative_to(source)).as_posix())


def refs_for(skill_md: Path) -> list[str]:
    text = skill_md.read_text(encoding="utf-8")
    return sorted(set(match.strip() for match in re.findall(r"Deep reference:\s+(.+?\.md)", text)))


def build_skill(root: Path, skill_dir: Path, out_zip: Path, include_agents: bool = True) -> None:
    if out_zip.exists():
        out_zip.unlink()
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in skill_dir.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(skill_dir)
            if not include_agents and rel.parts and rel.parts[0] == "agents":
                continue
            archive.write(path, rel.as_posix())

        for ref in refs_for(skill_dir / "SKILL.md"):
            ref_path = root / ref
            if ref_path.exists():
                archive.write(ref_path, ref_path.relative_to(root).as_posix())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--out", default="./dist")
    parser.add_argument("--claude", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = (root / args.out).resolve()
    skills_dir = root / "skills"
    version_path = root / "VERSION"
    version = version_path.read_text(encoding="utf-8").strip() if version_path.exists() else ""

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    skill_zips = []
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        out_zip = out / f"{skill_dir.name}.zip"
        build_skill(root, skill_dir, out_zip, include_agents=not args.claude)
        skill_zips.append(out_zip)
        print(f"built {out_zip}")

    bundle_name = "dankoe-claude-skills.zip" if args.claude else f"dankoe-skills-{version}.zip"
    if version or args.claude:
        bundle_path = out / bundle_name
        with zipfile.ZipFile(bundle_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for skill_zip in skill_zips:
                archive.write(skill_zip, skill_zip.name)
            for name in ("README.md", "VERSION", "LICENSE"):
                path = root / name
                if path.exists():
                    archive.write(path, name)
        print(f"bundle {bundle_path}")


if __name__ == "__main__":
    main()
