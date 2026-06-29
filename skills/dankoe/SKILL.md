---
name: dankoe
description: Dankoe one-person company toolkit main router with default IMA knowledge-base grounding. Use when the user asks about building a one-person company, personal brand, creator business, digital product, content engine, AI-assisted solo business, focus system, writing system, learning path through Dankoe materials, IMA-backed Dankoe knowledge retrieval, or turning interests/skills/knowledge into income. Triggers include /dankoe, Dankoe, Dan Koe, 一人公司, 个人品牌, 数字产品, 内容地图, 学习地图, IMA知识库, 从哪开始看, 写作系统, AI一人公司, and "把我自己产品化".
---

# dankoe

Act as the router for the Dankoe one-person company toolkit. Do not solve the business problem in this skill. Identify the user's current bottleneck and route to the most relevant workflow.

## Default IMA Source

All Dankoe workflow skills default to the same IMA knowledge base:

```text
Dankoe 终极版 | 深度觉醒（持续更新）
```

Users do not need to say this knowledge-base name. Route normal user requests directly to the right workflow skill; that downstream skill should retrieve from IMA by default before producing the final output.

Use `$dankoe-ima` only when the user specifically wants source search, IMA troubleshooting, retrieval summaries, or a pure "find/read from IMA first" task.

## Route Map

| User intent | Route to | Use when |
|---|---|---|
| Wants a full one-person company path | `$dankoe-roadmap` | The user asks what to build, where to start, or how to turn interests, skills, problems, or knowledge into a business. |
| Wants guidance through the Dankoe knowledge base | `$dankoe-learning-map` | The user asks where to start, what to read first, which materials fit self-media/AI/product/offer goals, or asks questions while learning. |
| Wants source retrieval or IMA troubleshooting | `$dankoe-ima` | The user explicitly asks to search/read IMA, debug IMA setup, list retrieval evidence, or answer a pure source question. |
| Wants to package, price, or sell something | `$dankoe-offer` | The user has a skill, service, course idea, digital product, coaching idea, newsletter, community, or client service to monetize. |
| Wants audience growth or content ideas | `$dankoe-content` | The user asks about personal brand, content map, writing, newsletters, posts, audience building, or not running out of ideas. |
| Wants to write a specific essay, newsletter, thread, script, or posts | `$dankoe-writing` | The user has an idea, topic, note, transcript, article draft, or content angle and wants it turned into sharp writing. |
| Wants AI workflows for a solo business | `$dankoe-ai-system` | The user asks how to use AI to research, write, build, sell, operate, learn faster, or systemize a one-person business. |

## Clarify Once

If the user says only "帮我做 Dankoe 一人公司" or is otherwise vague, ask one question:

> 你现在最想推进哪一块：IMA资料检索、学习路径、路线图、产品报价、内容增长、具体写作，还是 AI 工作流？

After the answer, route immediately.

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
