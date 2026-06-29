---
name: dankoe-content
description: Build a Dankoe-style content engine for one-person companies with default IMA knowledge-base grounding. Use when the user wants content strategy, personal brand growth, audience building, content maps, newsletters, essays, social posts, YouTube ideas, writing systems, authentic ideas, or a repeatable content ecosystem that leads to offers. Triggers include /dankoe-content, 内容地图, 个人品牌, 写作系统, newsletter, content engine, audience growth, never run out of ideas.
---

# dankoe-content

Help the user build a content engine that turns their learning, problems, opinions, and proof into audience growth and buyer trust.

## Core Premise

Content is not random posting. It is a public thinking system:

```text
Problem -> Perspective -> Proof -> Practical lesson -> Offer bridge
```

The user does not need infinite ideas. They need a map of repeatable themes and a habit of converting lived experience into useful public artifacts.

## Default IMA Source

Before building the content map, retrieve source evidence from IMA by default.

- Default knowledge base: `Dankoe 终极版 | 深度觉醒（持续更新）`.
- Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for actual retrieval.
- Search the default knowledge base by exact name, then search 2 to 5 queries around content map, personal brand, writing, audience growth, and the user's topic.
- Use retrieved titles/snippets to ground pillars, long-form topics, and content-system recommendations.
- If IMA is unavailable, credentials are missing, or access fails, state that limitation and continue from the bundled abstract reference.
- Never expose `knowledge_base_id`, `media_id`, `folder_id`, or credentials.

## Intake

Ask for missing information:

```text
1. What do you want to be known for?
2. Who should care?
3. What offer or future offer should content support?
4. Which platform matters first?
5. Can you publish long-form, short-form, or both?
6. What are 5 problems you have solved or are currently solving?
```

## Workflow

### Phase 1: Content Position

Create a content position:

```text
I explore {domain} for {audience} who want {result}, from the point of view that {strong belief}.
```

Reject generic themes that have no point of view.

### Phase 2: Content Map

Build 4 layers:

- Core problem: what the audience wants fixed.
- Belief shift: what they misunderstand.
- Mechanism: how the user thinks the result is created.
- Proof and story: personal examples, client examples, experiments, failures.

### Phase 3: Pillars

Create 3 to 5 content pillars:

- Problem education
- Personal transformation
- Tactical how-to
- Opinion or worldview
- Proof, case study, or build-in-public
- Offer education

Each pillar needs example post ideas, not just labels.

### Phase 4: Long-To-Short System

Prefer a content ecosystem:

1. One weekly long-form essay, newsletter, script, or memo.
2. Extract 5 to 10 short posts from it.
3. Turn strong replies and objections into the next long-form piece.
4. Bridge some posts to the offer without making every post an ad.

If the user needs one specific essay, newsletter, thread, script, or post set written now, route to `$dankoe-writing` after the content map is clear.

### Phase 5: 30-Day Publishing Plan

Output:

- 4 weekly long-form topics
- 20 short-form post ideas
- 5 proof posts
- 5 offer bridge posts
- 1 weekly review question set

## Output Template

```markdown
# Dankoe 内容地图

## Content Position

## Audience Problem

## Strong Belief

## Content Pillars
1.
2.
3.

## Weekly Long-Form Queue

## Short-Form Ideas

## Offer Bridges

## 30-Day Publishing Plan

## Review Metrics
- Saves/bookmarks:
- Replies:
- Profile clicks:
- Email signups:
- Buyer conversations:
```

## Quality Bar

- Do not optimize for virality without buyer relevance.
- Do not create pillars that are just categories.
- Make the user's perspective sharper before making the schedule bigger.
- Content should lead to trust, not just attention.

## Route Next

- If content needs a product destination, route to `$dankoe-offer`.
- If the user wants a specific piece written, route to `$dankoe-writing`.
- If content production needs leverage, route to `$dankoe-ai-system`.
- If the user has no clear direction, route to `$dankoe-roadmap`.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_内容地图.md
