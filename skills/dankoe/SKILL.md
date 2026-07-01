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
