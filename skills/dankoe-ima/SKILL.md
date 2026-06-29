---
name: dankoe-ima
description: Bridge IMA knowledge-base retrieval with Dankoe workflows. Use when the user wants to search, read, cite, or use materials from an IMA knowledge base before running Dankoe learning-map, writing, offer, content, roadmap, or AI-system workflows. Triggers include /dankoe-ima, IMA Dankoe, 搜索IMA里的Dankoe, 从IMA知识库找资料, 结合IMA资料写作, 先检索知识库再做学习路线, Dankoe知识库问答.
---

# dankoe-ima

Bridge the user's IMA knowledge base with the Dankoe skill toolbox.

Your job is not to replace `ima-skill`. Your job is to orchestrate:

```text
IMA search/read -> evidence summary -> Dankoe workflow routing -> final answer
```

## Required Dependency

Use `ima-skill` for all IMA operations. When actual search, browsing, file upload, or original-content reading is needed, load and follow:

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

Do not invent IMA APIs. Do not expose internal `knowledge_base_id`, `media_id`, or `folder_id` to the user.

If `ima-skill` is not installed or credentials are missing, instruct the user:

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

Credentials must be configured through the official IMA skill/API flow. Never ask the user to paste an API Key into a public file, README, GitHub issue, screenshot, or shared chat.

## Default Knowledge Base

Default target knowledge base name:

```text
Dankoe 终极版 | 深度觉醒（持续更新）
```

Users do not need to mention this default knowledge base in each prompt. When the user invokes `$dankoe-ima` without naming a knowledge base, silently use the default target knowledge base.

If the user names another IMA knowledge base, use that name instead.

If the default name is available, use it directly. If multiple matching knowledge bases are found for a non-default or partial name, do not auto-select the first or largest result. Show the visible knowledge-base names and ask the user to choose. Prefer exact name matches only when there is a single unambiguous result.

If no matching knowledge base is found, tell the user to create/upload one in IMA, or ask for the correct knowledge-base name.

## Core Workflow

### Phase 1: Intent Classification

Classify the user's request:

- Learning route: route to `$dankoe-learning-map`.
- Writing: route to `$dankoe-writing`.
- Offer/product: route to `$dankoe-offer`.
- Content strategy: route to `$dankoe-content`.
- One-person company roadmap: route to `$dankoe-roadmap`.
- AI workflow: route to `$dankoe-ai-system`.
- Pure source question: answer from IMA retrieval, then suggest next route if useful.

### Phase 2: Search Query Design

Turn the user's request into 2 to 5 IMA search queries.

Examples:

| User request | IMA search queries |
|---|---|
| 我是做自媒体的，先看哪些 | `个人品牌`, `内容地图`, `2 Hour Writer`, `从0涨粉`, `真实内容` |
| 帮我写个人品牌文章 | `个人品牌`, `内容地图`, `2 Hour Writer`, `信任`, `受众增长` |
| 设计数字产品 offer | `Mental Monetization`, `Make It Profitable`, `推出产品`, `landing page` |

### Phase 3: IMA Retrieval

Use `ima-skill` knowledge-base search.

Search rules:

- Search the target knowledge base by name first if needed.
- If the target knowledge-base name is ambiguous, stop and ask the user to pick by visible name. Do not use role, creator, member count, or content count as silent selection criteria.
- Search multiple queries rather than one broad query.
- Prefer titles and snippets first.
- Read original content only when the task requires specific source detail.
- For unsupported media or unavailable original content, summarize from search results and clearly state the limitation.

### Phase 4: Evidence Summary

Before routing to a Dankoe workflow, create an evidence block:

```markdown
## IMA 检索摘要
- 知识库：
- 检索词：
- 命中的材料：
- 可用证据：
- 不确定/缺失：
```

Do not quote long source passages. Use short snippets only when necessary, then paraphrase.

### Phase 5: Route To Dankoe Workflow

After evidence summary, apply the relevant Dankoe workflow:

- `$dankoe-learning-map`: build learning path from retrieved source titles/snippets.
- `$dankoe-writing`: turn retrieved ideas into an article, post, script, or newsletter.
- `$dankoe-offer`: turn retrieved method into a sellable product/service.
- `$dankoe-content`: turn retrieved ideas into content map and topic system.
- `$dankoe-roadmap`: connect source ideas to one-person company roadmap.
- `$dankoe-ai-system`: turn source ideas into AI workflow.

If a downstream skill is needed, say:

```text
我已经从 IMA 找到资料。下一步按 $skill-name 的流程处理。
```

Then execute that workflow in the same answer when enough context exists.

## Upload Guidance

If the user asks how to make IMA readable:

1. Create an IMA knowledge base named `Dankoe 终极版 | 深度觉醒（持续更新）`, or tell `$dankoe-ima` the name of their own knowledge base.
2. Upload supported files such as PDF, DOCX, PPTX, Markdown, or text files.
3. Do not upload YouTube/Bilibili links through OpenAPI; use the IMA desktop client for unsupported media.
4. Keep original filenames; IMA upload rules require title to equal file name.

If the user asks you to upload files, use `ima-skill` and follow its file-upload gates.

## Output Template

```markdown
# Dankoe IMA 检索结果

## 你的问题

## IMA 检索摘要
- 知识库：
- 检索词：
- 命中的材料：
- 可用证据：
- 不确定/缺失：

## 工作流判断
应该进入：$skill-name

## 处理结果

## 下一步
```

## Quality Bar

- Never claim to have read IMA content unless retrieval actually happened.
- Never rely on the user's private local path unless the user provides it and asks for local-file reading.
- Always distinguish "IMA retrieval evidence" from "Dankoe workflow inference".
- If IMA credentials are missing, explain setup and continue with the bundled abstract knowledge pack only if the user accepts.
- Do not expose internal IMA IDs.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_IMA桥接.md
