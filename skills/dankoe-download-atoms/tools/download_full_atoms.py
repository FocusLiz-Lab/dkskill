#!/usr/bin/env python3
"""Download the full atom libraries for this skill from the latest GitHub Release."""

from __future__ import annotations

import sys
import urllib.request
import zipfile
import tempfile
from pathlib import Path

REPO = "FocusLiz-Lab/dkskill"
ASSET_URL = f"https://github.com/{REPO}/releases/latest/download/dks-local.zip"
INSTALL_PREFIX = "知识库/原子库/"


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def download(url: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as response:
        target.write_bytes(response.read())


def normalize_member(name: str) -> str:
    normalized = name.replace("\\", "/")
    return normalized.split("/", 1)[1] if normalized.startswith("dks/") else normalized


def install_from_zip(zip_path: Path) -> int:
    count = 0
    root = package_root()
    with zipfile.ZipFile(zip_path) as archive:
        for member in archive.infolist():
            relative = normalize_member(member.filename)
            if member.is_dir() or not relative.startswith(INSTALL_PREFIX):
                continue
            if not (relative.endswith(".jsonl") or relative.endswith(".json") or relative.endswith(".md")):
                continue
            data = archive.read(member)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            count += 1

            sibling_root = root.parent / "dankoe"
            if sibling_root.exists():
                sibling_target = sibling_root / relative
                sibling_target.parent.mkdir(parents=True, exist_ok=True)
                sibling_target.write_bytes(data)
    return count


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        zip_path = Path(tmp) / "dks-local.zip"
        print(f"下载 {ASSET_URL} ...")
        download(ASSET_URL, zip_path)
        count = install_from_zip(zip_path)

    if count == 0:
        print("未下载到任何原子库文件。", file=sys.stderr)
        return 1
    print(f"完成：已安装 {count} 个文件到 {package_root() / '知识库'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
