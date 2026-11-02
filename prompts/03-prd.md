# 03 – PRD

## Prompt

```
Read docs/ carefully: the lecture 2 summary (section 11 describes this assignment),
docs/concept-brief.md (our full concept - follow it) and docs/team-roles.md.
Then write PRD.md in the project root: a full Product Requirements Document for Exercise 1.

Project: a marketing campaign presentation for AURA, a fictional lip tint brand.
Concept: "natural glow from within" + food-inspired branding. Slogan (draft): "Your glow, freshly made."
Shades (draft): Honey Glaze, Peach Nectar, Berry Juice, Pomegranate Drop, Cocoa Kiss.

Deliverables:
1. HTML presentation (owner: Raghad): single HTML file, Hebrew, strict RTL + correct BiDi,
   up to 15 slides, navigation buttons (next/previous/home) in JavaScript.
   Part A: case study of Rhode's food-inspired marketing and its Lip Tint (factual analysis only).
   Part B: the AURA campaign: brief, target persona, insight, positioning, the ad, pricing/KPIs.
2. 3D animated ad (owner: Raneem): Three.js, 15-20 seconds, AURA tube with floating
   fruits/honey that emit a glowing "aura" in each shade color, Hebrew captions, sound effects.
   Embedded in the presentation.
3. Python (owner: Raghad): a simulation of 1,000 customers choosing between food-named shades
   and numbered shades (e.g. "Berry Juice" vs "Shade #03"), shown as a chart.
   The presentation must run it (preferably in the browser with Pyodide, with a "Run" button).

Rules to include: the Rhode part is analysis only, with no Rhode logos, product images or photos
of real people anywhere in our files; AURA's visuals are fully original. Keep prompts short to save tokens.
Versioning (v1, v2...), every prompt saved in prompts/, README.md updated on every push
with screenshots, and a "red team" review by a different LLM before submission.
Include: goals, scope and out-of-scope, file structure, work split, milestones,
and acceptance criteria for each deliverable.

Also save this prompt in prompts/03-prd.md.

Before pushing:
- Show me a summary of the changes and wait for my approval.
- Write a commit message with a short title, plus 2-3 lines explaining
  what changed, why, and whether it is a critical change or a minor one.
- Add a line to the "Progress Log" section in README.md with the date
  and what was done in this step.
After I approve, commit and push to GitHub.
```

## Note on what was done

- Read `docs/concept-brief.md`, `docs/team-roles.md` and section 11 of the lecture 2 summary (what to submit, PRD as the "contract", GitHub/README/prompt-chain requirements, scope and what is really graded).
- Wrote `PRD.md` (v1): summary, goals, scope / out-of-scope, content and IP rules, the three deliverables with acceptance criteria, file structure, work split, milestones M0–M8, red-team process, Definition of Done, risks and open decisions.
- Changes from the concept brief: added a campaign brief slide, a positioning statement and a pricing slide, so Part B is complete within 15 slides. Added a cocoa bean to the film, so all 5 shades get an aura.
- Added the Progress Log line in `README.md`. Pushed only after approval.
