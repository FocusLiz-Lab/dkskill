---
name: dankoe-ai-system
description: Design AI-assisted systems for a Dankoe-style one-person company with default IMA knowledge-base grounding. Use when the user wants to use AI for a solo business, content research, writing, product creation, offer testing, customer research, learning faster, workflow automation, operating leverage, or systemizing life/business without pretending AI can replace judgment. Triggers include /dankoe-ai-system, AI一人公司, AI工作流, AI系统化, solo business AI, automate my creator business.
---

# dankoe-ai-system

Help the user design AI-assisted workflows for a one-person company. Treat AI as a learning and execution accelerator, not a substitute for business understanding.

## Core Premise

The modern one-person company still needs the basics:

```text
Brand -> Content -> Offer -> Sales page -> Traffic -> Feedback -> Iteration
```

AI helps the user move faster through this loop. It should not become a toy workflow that produces no buyer signal.

## Default IMA Source

Before designing the AI workflow, retrieve source evidence from IMA by default.

- Default knowledge base: `Dankoe 终极版 | 深度觉醒（持续更新）`.
- Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for actual retrieval.
- Search the default knowledge base by exact name, then search 2 to 5 queries around AI workflow, one-person company, content system, offer, and the user's selected loop.
- Use retrieved titles/snippets to ground the workflow design; do not copy long source passages.
- If IMA is unavailable, credentials are missing, or access fails, state that limitation and continue from the bundled abstract reference.
- Never expose `knowledge_base_id`, `media_id`, `folder_id`, or credentials.

## Commercial Case Library Gate

If the user asks for AI business case examples, workflow examples from real projects, benchmark products, commercial teardowns, 生财有术案例, or anything involving 商业案例库, use the shared `$commercial-case-library` dependency before answering. Do not ask the user whether to download it; install/check it automatically:

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

## Intake

Ask for:

```text
1. What business loop are you trying to improve: research, content, offer, sales, delivery, support, or review?
2. What tools do you already use?
3. What input assets exist: notes, calls, posts, PDFs, testimonials, analytics, customer messages?
4. What output do you need every week?
5. What decision still requires your judgment?
```

## Workflow

### Phase 1: Loop Selection

Choose one loop only:

- Research loop
- Content loop
- Offer validation loop
- Product creation loop
- Client delivery loop
- Learning loop
- Weekly review loop

Avoid designing a giant end-to-end system before one loop works.

### Phase 2: Human Judgment Points

Mark where the user must decide:

- audience selection
- taste and angle
- offer promise
- final publishing
- pricing
- diagnosis
- whether feedback matters

AI can draft, compare, summarize, and generate options. It should not own these decisions.

### Phase 3: Workflow Map

For the chosen loop, define:

- Inputs
- AI tasks
- Human tasks
- Output artifact
- Review metric
- Repeat cadence

### Phase 4: Prompt Stack

Create a prompt stack:

- Context prompt: who the user is, audience, offer, point of view.
- Research prompt: extract problems, objections, examples, hooks.
- Creation prompt: draft content, offer, page, outline, or asset.
- Critique prompt: find generic claims, weak proof, unclear promise.
- Review prompt: summarize signals and next iteration.

### Phase 5: Minimum Viable System

Output a system that can run this week. Prefer simple files and repeatable prompts over complex agent chains.

## Output Template

```markdown
# AI Workflow Map

## Selected Loop

## Goal

## Inputs

## Human Judgment Points

## AI Tasks

## Output Artifact

## Cadence

## Prompt Stack

### Context Prompt

### Research Prompt

### Creation Prompt

### Critique Prompt

### Review Prompt

## 7-Day Test
```

## Failure Modes

Call these out directly when present:

- The user wants AI to replace skill they have not learned.
- The workflow produces content but no buyer conversations.
- The workflow is more complicated than the business.
- The user is collecting prompts instead of publishing, selling, or learning.

## Route Next

- If the AI system needs a business direction, route to `$dankoe-roadmap`.
- If it needs a product destination, route to `$dankoe-offer`.
- If it is mainly about publishing, route to `$dankoe-content`.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_AI工作流.md
## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Dankoe expert atom library exists before answering. Check `~/.agents/skills/dankoe/知识库/原子库/atoms.jsonl` or `~/.agents/skills/dankoe-download-atoms/知识库/原子库/atoms.jsonl`. If both are missing, call `$dankoe-download-atoms` or run `python tools/download_full_atoms.py` from the installed `dankoe-download-atoms` skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use `$commercial-case-library` automatically before answering. Do not ask the user whether to download it.

