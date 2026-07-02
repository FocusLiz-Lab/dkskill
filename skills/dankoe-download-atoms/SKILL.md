---
name: dankoe-download-atoms
description: 下载或更新 Dan Koe / dkskill 的全量本地专家原子库。用于用户安装 SkillHub 轻量包后，需要从 GitHub 拉取完整 `知识库/原子库/atoms.jsonl` 和按年份/季度拆分的 `atoms_*.jsonl`。商业案例库已抽离为共享依赖 `$commercial-case-library`，不要在本 skill 内重复下载。
---

# dankoe-download-atoms 全量专家原子库下载

当用户要求下载、补全、更新或修复 dkskill 本地专家原子库，或 IMA 不可用需要本地兜底时，自动运行：

```powershell
python .\tools\download_full_atoms.py
```

运行目录应为 `dankoe-download-atoms` skill 目录本身。脚本会直接下载 GitHub Release 的 `dks-local.zip` 并解压 `知识库/原子库/`，不使用 GitHub contents API，因此不会因为 contents API rate limit 导致 403。

不要询问用户是否下载；当本地原子库缺失且需要本地兜底时，直接下载。只有网络、权限或文件系统写入失败时才停止并展示错误。

如果用户需要商业案例、案例拆解、对标案例、变现案例或生财有术案例，不要在这里下载。改用：

```text
$commercial-case-library
```

下载完成后，原子库应位于：

```text
知识库/原子库/atoms.jsonl
```

以及同目录下的 `atoms_*.jsonl` 文件。


