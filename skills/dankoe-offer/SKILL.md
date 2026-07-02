---
name: dankoe-offer
description: Design Dankoe-style offers for one-person companies with default IMA knowledge-base grounding. Use when the user wants to turn a skill, knowledge, service, consulting idea, coaching idea, newsletter, course, template, community, or digital product into a sellable offer with a clear buyer, promise, mechanism, price, delivery scope, and validation plan. Triggers include /dankoe-offer, 报价设计, 数字产品, 产品化, 变现, offer, landing page, sell my knowledge.
---

# dankoe-offer

Help the user turn knowledge, skill, or lived experience into a sellable offer. The goal is not to brainstorm many ideas. The goal is to produce one offer that can be tested.

## Core Premise

An offer is a promise attached to a buyer, a painful problem, a believable mechanism, a delivery container, and a price.

```text
Buyer -> Pain -> Desired result -> Mechanism -> Proof -> Container -> Price -> Test
```

## Default IMA Source

Before designing the offer, retrieve source evidence from IMA by default.

- Default knowledge base: `Dankoe 终极版 | 深度觉醒（持续更新）`.
- Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for actual retrieval.
- Search the default knowledge base by exact name, then search 2 to 5 queries around offer, monetization, buyer problem, product, and the user's niche.
- Use retrieved titles/snippets to ground the offer mechanism and validation plan.
- If IMA is unavailable, credentials are missing, or access fails, state that limitation and continue from the bundled abstract reference.
- Never expose `knowledge_base_id`, `media_id`, `folder_id`, or credentials.

## Commercial Case Library Gate

If the user asks for offer examples, pricing examples, business case references, product teardowns, benchmark offers, monetization cases, 生财有术案例, or anything involving 商业案例库, use the shared `$commercial-case-library` dependency before answering. Do not ask the user whether to download it; install/check it automatically:

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

Collect only what is missing:

```text
1. Who do you want to help?
2. What painful problem can you help them solve?
3. What result can you credibly help them reach?
4. What proof do you have?
5. Do you want to sell service, consulting, coaching, course, template, subscription, or community?
```

## Workflow

### Phase 1: Buyer Specificity

Reject vague buyers such as "creators", "people who want to grow", "ordinary people", or "everyone interested in AI." Narrow by situation:

- current pain
- urgency
- ability to pay
- existing behavior
- reachable channel

### Phase 2: Problem Quality

Score the problem:

- Is it urgent?
- Is it expensive if ignored?
- Does the buyer already try to solve it?
- Can the user produce a visible result?
- Can the user get proof within 30 days?

If fewer than 3 are true, redesign the problem before designing the product.

### Phase 3: Offer Type

Choose one:

- Done-for-you service: for speed, proof, and cash.
- Done-with-you consulting/coaching: for diagnosis-heavy problems.
- Digital product: for repeatable methods with existing audience.
- Template/toolkit: for structured execution.
- Subscription/community: for ongoing identity, accountability, or curation.

For new creators with no audience, prefer service or consulting before courses.

### Phase 4: Offer Card

Create a one-page offer card:

- Buyer
- Pain
- Promise
- Mechanism
- Deliverables
- Timeline
- Price
- Guarantee or risk reversal
- Who it is not for
- First validation action

### Phase 5: Validation Plan

Do not declare the offer "good" until it meets a market signal:

- 5 buyer conversations
- 3 direct objections collected
- 1 paid pilot
- 10 qualified landing page visits with feedback
- 1 testimonial or case result

## Output Template

```markdown
# Offer Card

## Buyer

## Pain

## Promise

## Mechanism

## Container
- Format:
- Timeline:
- Deliverables:
- Support:

## Price

## Proof Needed

## Landing Page Spine
1. Pain:
2. New mechanism:
3. Promise:
4. What they get:
5. Why now:
6. CTA:

## 7-Day Validation Plan
```

## Quality Bar

- The promise must be specific enough to be judged.
- The price must match the buyer and delivery burden.
- The delivery scope must be narrow enough for one person.
- The first version should be ugly but sellable, not complete but untested.

## Route Next

- If the user needs traffic for the offer, route to `$dankoe-content`.
- If the user needs delivery leverage, route to `$dankoe-ai-system`.
- If the user lacks a clear business direction, route to `$dankoe-roadmap`.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_offer框架.md
## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Dankoe expert atom library exists before answering. Check `~/.agents/skills/dankoe/知识库/原子库/atoms.jsonl` or `~/.agents/skills/dankoe-download-atoms/知识库/原子库/atoms.jsonl`. If both are missing, call `$dankoe-download-atoms` or run `python tools/download_full_atoms.py` from the installed `dankoe-download-atoms` skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use `$commercial-case-library` automatically before answering. Do not ask the user whether to download it.

