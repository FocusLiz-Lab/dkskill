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
