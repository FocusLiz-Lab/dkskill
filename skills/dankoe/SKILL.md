---
name: dankoe
description: Dankoe 一人公司 Skill 工具箱主入口。用于个人品牌、创作者商业、数字产品、内容系统、AI 辅助一人公司、专注系统、写作系统、学习路径、IMA 资料检索，以及把兴趣、技能和知识转成收入。默认使用 IMA 知识库「Dankoe 终极版 | 深度觉醒（持续更新）」，并可在 IMA 不可用时读取本地原子库。触发词包括 /dankoe、Dankoe、Dan Koe、一人公司、个人品牌、数字产品、内容地图、学习地图、IMA知识库、写作系统、AI一人公司和“把我自己产品化”。
---

# dankoe 一人公司工具箱

这是 Dankoe 一人公司工具箱的主入口。先识别用户当前卡点，再路由到最相关的 workflow；如果上下文足够，直接执行对应工作流。

## 默认 IMA 资料源

所有 Dankoe workflow skills 默认读取同一个 IMA 知识库：

```text
Dankoe 终极版 | 深度觉醒（持续更新）
```

用户不需要每次输入这个知识库名称。普通请求应直接路由到合适的 workflow skill；下游 skill 默认先检索 IMA，再输出结果。

只有当用户明确要资料检索、IMA 排错、检索摘要，或纯粹要求“先从 IMA 找资料”时，才使用 `$dankoe-ima`。

## 路由表

| User intent | Route to | Use when |
|---|---|---|
| Wants a full one-person company path | `$dankoe-roadmap` | The user asks what to build, where to start, or how to turn interests, skills, problems, or knowledge into a business. |
| Wants guidance through the Dankoe knowledge base | `$dankoe-learning-map` | The user asks where to start, what to read first, which materials fit self-media/AI/product/offer goals, or asks questions while learning. |
| Wants source retrieval or IMA troubleshooting | `$dankoe-ima` | The user explicitly asks to search/read IMA, debug IMA setup, list retrieval evidence, or answer a pure source question. |
| Wants to package, price, or sell something | `$dankoe-offer` | The user has a skill, service, course idea, digital product, coaching idea, newsletter, community, or client service to monetize. |
| Wants audience growth or content ideas | `$dankoe-content` | The user asks about personal brand, content map, writing, newsletters, posts, audience building, or not running out of ideas. |
| Wants to write a specific essay, newsletter, thread, script, or posts | `$dankoe-writing` | The user has an idea, topic, note, transcript, article draft, or content angle and wants it turned into sharp writing. |
| Wants AI workflows for a solo business | `$dankoe-ai-system` | The user asks how to use AI to research, write, build, sell, operate, learn faster, or systemize a one-person business. |

## Concept Explanation Fast Path

If the user asks what a Dankoe idea, essay, video, course section, philosophy, focus concept, life-design concept, or abstract principle "means" and wants it explained in plain language, treat it as a learning/explanation task, not a business case task.

Use this fast path before the commercial case gate, before broad IMA troubleshooting, and before general learning-plan templates:

1. Route to `$dankoe-learning-map` unless the user asks to write publishable content.
2. Use the local Dankoe atom library first when it is already installed. Search only the most specific title/phrase and 1 to 2 adjacent concepts, such as `专注的艺术`, `Art of Focus`, `attention`, `purpose`, or `深度工作`.
3. Do not install, check, or search `$commercial-case-library` for pure philosophy, focus, attention, meaning, life design, or concept-explanation questions unless the user explicitly asks for business cases or monetization examples.
4. Do not run a full library bootstrap when either `~/.agents/skills/dankoe/知识库/原子库/atoms.jsonl` or `~/.agents/skills/dankoe-download-atoms/知识库/原子库/atoms.jsonl` already exists.
5. Answer in plain language once, then optionally add a short "怎么用" section.
6. Do not also output a learning roadmap, "先看哪个", "7 天启动计划", or a second recommendation block unless the user explicitly asks what to read next.

## Commercial Case Library Gate

If the user's request needs commercial cases, business examples, benchmark projects, case studies, teardown examples, market examples, monetization examples, 生财有术案例, or asks to "找案例/拆案例/参考案例/对标/商业案例库", treat the commercial case atom library as a required dependency. Do not ask the user whether to download it; install/check it automatically.

Additional trigger rule: if the user asks about acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, or which platform to publish on, assume case evidence would improve the answer. Use `$commercial-case-library` automatically before answering, without asking the user whether to download it.

Before answering or routing, use the shared `$commercial-case-library` dependency. Check whether this shared file exists:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If the shared library is missing, do not ask for confirmation. Automatically ensure the dependency is available:

1. If `$commercial-case-library` is not installed or cannot be loaded, install it immediately without asking the user:

```text
npx -y skills add FocusLiz-Lab/commercial-case-library -g --all
```

2. Run the shared downloader:

```text
python scripts/download_cases.py
```

3. Continue the original task after the download succeeds.

Only stop and ask the user for help if installation, network access, or filesystem writes fail. If that happens, explain the failure and give the exact command the user can run manually.

## Local Atom Bootstrap

For source-grounded Dankoe answers, prefer IMA first. If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local expert atom library is available before answering.

Check for either of these files:

```text
~/.agents/skills/dankoe/知识库/原子库/atoms.jsonl
~/.agents/skills/dankoe-download-atoms/知识库/原子库/atoms.jsonl
```

GitHub installs of `dkskill` should already include the local expert atom library under `~/.agents/skills/dankoe/知识库/原子库/`. If both files are missing, treat the install as a light/partial install and call `$dankoe-download-atoms` or run this from the installed `dankoe-download-atoms` skill directory:

```powershell
python tools/download_full_atoms.py
```

Do not ask the user whether to download the expert atom library. Download automatically when it is required for local fallback. Only stop if installation, network access, or filesystem writes fail.

## 只澄清一次

如果用户只说“帮我做 Dankoe 一人公司”或需求过于模糊，只问一个问题：

> 你现在最想推进哪一块：IMA资料检索、学习路径、路线图、产品报价、内容增长、具体写作，还是 AI 工作流？

收到回答后，立即路由到对应 workflow。

## Boundary Rules

- Do not present Dankoe material as magic automation. AI accelerates learning and execution; it does not replace strategy, taste, proof, or iteration.
- Do not encourage vague "one-person company" identity work without a sellable offer or audience-building loop.
- Do not copy long passages from the local Dankoe PDFs. Use them as source material for abstracted workflows only.
- Prefer concrete outputs: route, diagnosis, one-page plan, offer card, content map, essay outline, finished draft, workflow map, or next-week actions.

## Standard Handoff

Use this handoff format:

```text
这个问题交给 $skill-name。
原因：{one sentence}
需要输入：{what the user should provide next}
```
## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Dankoe expert atom library exists before answering. GitHub installs should already include it under `~/.agents/skills/dankoe/知识库/原子库/atoms.jsonl`. Also check `~/.agents/skills/dankoe-download-atoms/知识库/原子库/atoms.jsonl`. If both are missing, treat this as a light/partial install and call `$dankoe-download-atoms` or run `python tools/download_full_atoms.py` from the installed `dankoe-download-atoms` skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use `$commercial-case-library` automatically before answering. Do not ask the user whether to download it.

Do not use `$commercial-case-library` for pure Dankoe philosophy, focus, attention, meaning, life-design, learning, or concept-explanation questions unless the user explicitly asks for cases, benchmarks, monetization examples, or platform/channel decisions.

## Dankoe Methodology First

Every answer must use Dankoe methodology as the primary reasoning layer. For `/dankoe` requests, first ground the diagnosis, framing, and recommendation in Dankoe sources or Dankoe workflow principles:

1. Prefer the default IMA knowledge base `Dankoe 终极版 | 深度觉醒（持续更新）`.
2. If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or local fallback is needed, use the local Dankoe expert atom library and auto-bootstrap it when missing.
3. Only after the Dankoe layer is established, add commercial cases when the question would benefit from proof, benchmarks, platform/channel examples, monetization examples, acquisition examples, or Chinese-market context.
4. Commercial cases are supporting evidence only. Do not let commercial cases replace Dankoe methodology, and do not answer purely from the commercial case library unless no Dankoe source is available; if that happens, label the answer as case-supported inference rather than Dankoe-grounded.
5. In final answers, keep the distinction clear: `Dankoe 方法论` for the core principle and `商业案例支撑` for examples.


