---
name: dankoe-roadmap
description: Build a Dankoe-style one-person company roadmap with default IMA knowledge-base grounding. Use when the user wants to start or redesign a one-person business, turn themselves into a business, combine interests into a niche, choose a direction, create a personal brand path, or map the path from skill/interests/problems to audience, offer, and revenue. Triggers include /dankoe-roadmap, 一人公司路线图, 将自己产品化, niche, personal monopoly, creator business roadmap.
---

# dankoe-roadmap

Help the user turn their interests, skills, problems, and lived experience into a practical one-person company roadmap.

## Core Premise

A one-person company is not "one person doing every task forever." It is a simple value system:

```text
Identity and interests -> problems worth solving -> content proof -> offer -> feedback -> better product
```

AI and tools accelerate this loop, but the user still needs judgment, taste, proof, and repetition.

## Default IMA Source

Before producing the roadmap, retrieve source evidence from IMA by default.

- Default knowledge base: `Dankoe 终极版 | 深度觉醒（持续更新）`.
- Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for actual retrieval.
- Search the default knowledge base by exact name, then search 2 to 5 queries based on the user's direction.
- Use retrieved source titles/snippets to ground the roadmap; do not copy long source passages.
- If IMA is unavailable, credentials are missing, or access fails, state that limitation and continue from the bundled abstract reference.
- Never expose `knowledge_base_id`, `media_id`, `folder_id`, or credentials.

## Intake

Ask for missing information only once. Prefer this compact intake:

```text
1. 你现在会什么，或者正在学什么？
2. 你过去 2 年反复解决过什么问题？
3. 你愿意持续写/讲/研究什么主题？
4. 你现在有没有受众、客户、作品或收入？
5. 你每周能投入多少深度工作时间？
```

If the user already gave enough context, skip intake and proceed.

## Workflow

### Phase 1: Raw Material Audit

Separate the user's inputs into:

- Skills: what they can do for others.
- Interests: what they can study without forcing themselves.
- Problems: what they have solved or are solving.
- Proof: portfolio, results, audience, testimonials, or credible experience.
- Constraints: time, money, language, platform, energy, risk tolerance.

If there is no proof, do not fake authority. Design a proof-building path first.

### Phase 2: Niche Construction

Do not ask the user to "pick a niche" as a static category. Build a niche as a point of view:

```text
I help {specific people} move from {painful current state} to {desired state} through {mechanism I can prove or practice}.
```

Reject niches that are only labels, such as "AI", "self-growth", "finance", "creator economy", or "one-person company."

### Phase 3: Path Selection

Choose one primary path:

- Client service: fastest path when the user has no audience but can solve a valuable problem.
- Coaching/consulting: use when the user has judgment and can diagnose specific situations.
- Digital product: use when the user has repeated methods, templates, or teachable systems.
- Newsletter/community: use when the user can publish consistently and create belonging or curation value.
- Hybrid: use when service creates cash and proof, then product packages repeated solutions.

For beginners, prefer service first unless the user already has distribution.

### Phase 4: 90-Day Roadmap

Output a 90-day plan:

- Days 1-14: clarify point of view, publish proof-of-thinking, talk to potential buyers.
- Days 15-30: create first offer or service, get conversations, test objections.
- Days 31-60: publish around the buyer's problem, improve the offer, collect proof.
- Days 61-90: systemize delivery, create assets, decide whether to productize.

### Phase 5: First Week Actions

Always end with 3 to 5 concrete actions for the next 7 days. Each action must produce an artifact: a landing page draft, 10 posts, 5 outreach messages, 3 customer calls, an offer card, or a case study.

## Output Template

```markdown
# Dankoe 一人公司路线图

## 当前判断
- 阶段：
- 最大卡点：
- 不该做的事：

## 可用原材料
- 技能：
- 兴趣：
- 已解决问题：
- 证明：
- 约束：

## 定位句
我帮助 {人群} 从 {现状} 到 {结果}，方法是 {机制}。

## 推荐路径
{client service / consulting / digital product / newsletter / hybrid}

## 90 天路线
...

## 未来 7 天
...
```

## Route Next

- If the roadmap depends on monetization, route to `$dankoe-offer`.
- If the roadmap depends on publishing, route to `$dankoe-content`.
- If the roadmap depends on AI workflow design, route to `$dankoe-ai-system`.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_一人公司框架.md
