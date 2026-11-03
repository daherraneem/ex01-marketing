# PRD – Exercise 1: AURA Launch Campaign

**Course:** AI Agents & Vibe Coding (361.1005), University of Haifa – Dr. Yoram Segal
**Team:** Raneem Daher & Raghad Rabah
**Field:** Marketing communication
**Status:** v1 (draft) – 2026-11-02
**Sources:** `docs/concept-brief.md` (the concept – this PRD follows it), `docs/team-roles.md`, lecture 2 summary §11 (the assignment as described in class)

> This document is the "contract" with the client (the lecturer): what we deliver, how much, and how we will know it is done.

---

## 1. Summary

A Hebrew HTML presentation, **"We learned from Rhode, and built our own brand"**:

- **Part A** – one bridge slide on how Rhode uses food in its marketing: 2–3 short facts, each with a public source. We chose to keep Part A short and focus on our own brand, AURA.
- **Part B** – a launch campaign for **AURA**, our own fictional lip tint brand. It uses the same insight in an original way.

The presentation embeds a **3D animated ad** (Three.js). It also runs a **Python simulation** that tests the campaign's main idea with numbers: food names make people want to buy.

| | |
|---|---|
| **Brand** | AURA (הילה) – natural glow from within |
| **Concept** | "Your glow starts with what nourishes you". Every shade is named after a natural food that "gives glow" |
| **Slogan (draft)** | *Your glow, freshly made.* |
| **Product** | Lip Tint: sheer, juicy and natural-looking, like lips after eating fruit |
| **Tone** | Warm, natural, juicy and young. Not "cold luxury" |
| **Insight** | Food-based sensory marketing: when a product looks tasty and has a food name, it creates "appetite", meaning the wish to buy. People pay for the story (lecture 1, the attention economy) |

### Shades

Names, colors and foods from Raghad's deck (`deck-v1.html`). HEX is the main color, the middle of the tube's light-to-dark gradient.

| # | Shade | Hebrew name | Flavor / food | HEX (light → main → dark) |
|---|---|---|---|---|
| 01 | Golden Honey Glaze | דבש טהור | Honey | `#FFCF61` → **`#E69217`** → `#9C5304` |
| 02 | Velvet Peach Nectar | אפרסק עסיסי | Peach | `#FFB299` → **`#F26C4B`** → `#B33216` |
| 03 | Berry Crush Elixir | פירות יער | Strawberry and blueberry | `#FF7AA8` → **`#D42663`** → `#78072F` |
| 04 | Ruby Pomegranate Jewel | רימון רובי | Pomegranate | `#FF4760` → **`#BA1128`** → `#59020E` |
| 05 | Silk Cocoa Glaze | קקאו קטיפתי | Chocolate, cocoa and coffee beans | `#C47E54` → **`#784121`** → `#381906` |

**Brand palette:** cream `#FFF6EC`, honey-gold `#D9A441`, deep plum `#4A1E3A`. Soft light, juicy shine and a glowing "aura" around every object.

---

## 2. Goals

### 2.1 Product goals (what the audience should feel and understand)
1. Show that food-inspired naming and visuals are a real marketing strategy, using Rhode as the example.
2. Turn that insight into a complete, believable, **original** campaign for AURA.
3. Back the insight with an interactive demonstration (the Python simulation). Present it honestly as a model built on assumptions, not as real data.

### 2.2 Course goals (what is actually graded)
The technical requirements are only the entry threshold. The lecturer grades professionalism:
- **Planning** – this PRD, written before building.
- **Control of the process** – a clear, numbered chain of prompts in `prompts/`.
- **Visible progress on GitHub** – many meaningful pushes, each explaining what changed.
- **Dialogue with the agent** to improve the product (v1 → v2 → v3).
- **Creativity, originality and a personal voice** – the core of the grade.

### 2.3 Non-goals
- A perfect product. Scope is roughly 4–8 hours of work together ("the best is the enemy of the good").
- A real market study or real sales data.

---

## 3. Scope

### In scope
| # | Deliverable | Owner |
|---|---|---|
| D1 | HTML presentation (Hebrew, RTL, up to 15 slides) | Raghad Rabah |
| D2 | 3D animated ad (Three.js, 20–25 s) embedded in D1 | Raneem Daher |
| D3 | Python simulation (1,000 customers) run from inside D1 | Raghad Rabah |
| D4 | Project documentation: `PRD.md`, `README.md`, `prompts/`, screenshots, red-team review | Both |

### Out of scope
- Any Rhode logo, product image or packaging design, and any photo of a real person, **anywhere in the repo**.
- Photorealistic AI images or real video footage (costly in tokens and against the "objects, not pixels" approach).
- A real e-commerce site, real checkout or real customer data.
- Claims presented as real market research. All AURA figures (prices, KPIs, simulation effect) are labelled as assumptions or targets.
- Mobile-first design. The deck targets a laptop or projector at 16:9. Basic responsiveness is welcome but not required.

---

## 4. Content and IP rules (mandatory)

1. **Rhode = analysis only.** Text and analysis only, illustrated with **our own original graphics** (shapes, icons, color blocks). No logos, product photos, campaign images or photos of people.
2. **Rhode facts must be correct.** Every factual claim (launch dates, product names, campaigns) is checked against a public source. The source is listed in a "Sources" line on the slide or in the deck's sources slide/footer. If a fact cannot be verified, we leave it out. No invented facts.
3. **AURA is 100% original.** Name, tube, colors, film and copy are our own. The tube is built from Three.js geometry, not from images.
4. **No real people.** The persona "Noor" is illustrated with an abstract or iconic figure, not a photo.
5. **Course materials stay local.** The lecture summary PDF is git-ignored (lecturer's copyright) and is never pushed.
6. **Simulation honesty.** The "name effect" is a working assumption for the demo. The deck says so on the same slide.

---

## 5. Deliverable D1 – HTML Presentation (Raghad)

### 5.1 Technical requirements
- **One HTML file** (`src/deck-vN.html`) with inline CSS and JS. Only the film file (D2) and CDN libraries (Pyodide) are external.
- `<html lang="he" dir="rtl">`. All layout is RTL.
- **Correct BiDi:** English terms (AURA, Rhode, Lip Tint, `Shade #03`, *Your glow, freshly made.*) are wrapped in `<bdi>` or `<span dir="ltr">`, so punctuation and numbers do not jump to the wrong side.
- **Up to 15 slides**, and each slide has text + graphics.
- **Navigation in JavaScript:** Next / Previous / Home buttons, plus keyboard arrows. In RTL, "Next" sits on the left. A slide counter shows "n / 15".
- Brand palette and a Hebrew-friendly font (for example Heebo or Assistant, from Google Fonts).

### 5.2 Slide plan (15 slides)

| # | Slide | Content | Part |
|---|---|---|---|
| 1 | פתיחה – Opening | AURA, slogan, team names | – |
| 2 | השאלה – The question | Why do we "want to eat" beauty products? | A |
| ~~3~~ | ~~Case Study: Rhode~~ | Replaced by one bridge slide, see the note below | A |
| ~~4~~ | ~~Rhode ואוכל~~ | Replaced by one bridge slide, see the note below | A |
| ~~5~~ | ~~ה-Lip Tint של Rhode~~ | Replaced by one bridge slide, see the note below | A |
| 6 | התובנה – The insight | Food-based sensory marketing | A→B |
| 7 | בריף הקמפיין – Campaign brief | Objective, audience, key message, deliverables | B |
| 8 | מציגים: AURA | Name, meaning, concept + **positioning statement** | B |
| 9 | הגוונים – The shades | Five shades, color swatches and inspirations | B |
| 10 | קהל היעד – Persona | "Noor", 22, student (needs, habits, channels) | B |
| 11 | הפרסומת – The ad | **Embedded 3D film (D2)** | B |
| 12 | ההוכחה בנתונים – The proof | **Python simulation (D3)**: "Run" button, slider and chart | B |
| 13 | ערוצי הקמפיין – Channels | Instagram, TikTok, influencers, campus tasting stand | B |
| 14 | תמחור ומדדים – Pricing & KPIs | Fictional price point + KPIs: reach, engagement, conversion (targets) | B |
| 15 | תודה – Thank you | Slogan, team, link to the GitHub repo | – |

**Changes from the concept brief:** we added a campaign brief slide (7), a positioning statement (slide 8) and pricing (slide 14). With these, the deck covers the full Part B list (brief, persona, insight, positioning, ad, pricing/KPIs) and still has only 15 slides.

**Change after the red team review:** Part A is **one bridge slide** ("מההשראה למותג שלנו", slide 7 in the final deck) with 3 short facts about Rhode's food-inspired marketing, each with a public source (Glossy, NewBeauty), instead of the three Rhode slides planned above. We chose this because the project is about our own brand, AURA, and Rhode is only the inspiration. The final deck has 12 slides.

### 5.3 Acceptance criteria – D1
- [ ] One HTML file opens in Chrome and Edge without console errors.
- [ ] `dir="rtl"` on the root. Every mixed Hebrew/English line renders in the correct order (checked by eye on slides 1, 5, 9 and 12).
- [ ] 15 slides or fewer, and every slide has text + at least one graphic element.
- [ ] Next / Previous / Home work by button and by keyboard. Previous is disabled on slide 1 and Next on the last slide.
- [ ] Slide 11 plays the film (D2). Slide 12 runs the simulation (D3) and shows a chart.
- [ ] Part A has zero Rhode logos or images and zero photos of real people. Every Rhode fact has a source.
- [ ] All AURA numbers (price, KPIs, simulation effect) are labelled as assumptions or targets.
- [ ] Brand palette used consistently. Text is readable on a projector (contrast and size).

---

## 6. Deliverable D2 – 3D Animated Ad (Raneem)

### 6.1 Technical requirements
- **One HTML file** (`src/film-vN.html`), with Three.js loaded from a CDN (ES module import).
- **Length 20–25 seconds**, on a timeline (the final film, v3, is 24 s). Plays from start to end and then shows "Replay".
- **Built from objects, not images:** the tube, honey drop, peach, berries, pomegranate and cocoa bean are made from Three.js geometry and materials. The glowing "aura" in each shade color uses emissive materials, additive sprites or a bloom post-process.
- **Hebrew captions** in an HTML overlay (`dir="rtl"`), timed to the scenes.
- **Sound effects** made with the Web Audio API (synthesized chimes, whoosh, sparkle). They are original, with no licensing issues and no audio files. Browsers block autoplay with sound, so the film starts with a **"▶ הפעל" (Play)** button.
- **Embeddable:** works inside an `<iframe>` in slide 11 and fills the frame (responsive to the iframe size).
- Optional, if time allows: an "orbit camera" button that shows the film is live 3D and not video.

### 6.2 Storyboard

| Time | On screen | Sound | Caption (HE) |
|---|---|---|---|
| 0–3 s | Dark, warm background, soft light. The AURA tube appears and rotates slowly | Soft opening tone | – |
| 3–8 s | Honey drop, peach, berries, pomegranate and cocoa bean float in. Each one gives off a glowing aura in its shade color | Gentle chime per object | e.g. "מה שמזין אותך…" |
| 8–13 s | The auras swirl into the tube, which fills with color | Whoosh | e.g. "…הופך לזוהר" |
| 13–16 s | The tube opens, and a juicy line of tint is drawn in the air | Sparkle | – |
| 16–20 s | AURA logo, *Your glow, freshly made.* and "הזוהר שלך מתחיל כאן" | Closing tone | "הזוהר שלך מתחיל כאן" |

**Change from the concept brief:** we added a cocoa bean, so that all **five** shades (including Silk Cocoa Glaze) get an aura.

### 6.3 Acceptance criteria – D2
- [ ] Runs as one HTML file in Chrome and Edge without console errors, at a steady frame rate on a regular laptop.
- [ ] Total length is between 20 and 25 seconds, and the scenes follow the storyboard.
- [ ] Five food objects, each with an aura in its exact shade HEX.
- [ ] Hebrew captions render RTL and are readable. The English slogan is BiDi-isolated.
- [ ] At least four distinct sound effects, in sync with the scenes. The film starts with a Play click and has Replay at the end.
- [ ] No image textures of real products and no photos. All visuals are original geometry.
- [ ] Plays correctly when embedded in slide 11 of D1.

---

## 7. Deliverable D3 – Python Simulation (Raghad)

### 7.1 Question
Does a food name for a shade increase the wish to buy?

### 7.2 Model
- **1,000 virtual customers.** Each one sees two shelves with the same five colors:
  - **Shelf A (numbered):** `Shade #01` … `Shade #05`
  - **Shelf B (food names):** `Golden Honey Glaze` … `Silk Cocoa Glaze`
- **1,000 customers per shelf.** On Shelf A each customer buys with a base probability of **10%**. On Shelf B the probability goes up by the **"name effect"** (default **20%**, relative, so 10% → 12%). Both numbers are demo assumptions, not real data, and the slide says so.
- Output: the number of buyers per shelf.
- Fixed random seed, so the same name effect always gives the same result.
- **Chart:** a bar chart comparing Shelf A and Shelf B (buyers), in AURA colors, with Hebrew text in the correct right-to-left order.

### 7.3 How the deck runs it
- `final/simulation.py` is the source of truth. It also runs locally (`python final/simulation.py`) and saves the chart as a PNG.
- Slide 12 runs **the same code in the browser with Pyodide**: a **"הרץ סימולציה" (Run)** button, a loading indicator while Pyodide loads, then the chart.
- A **slider** for the name effect (0%–30%, default 20%). After the first run, moving it re-runs the simulation and updates the chart.
- The Python code is embedded in the deck (identical to `simulation.py`). This keeps the deck a single file that works from `file://` without a local server.

### 7.4 Acceptance criteria – D3
- [ ] `python final/simulation.py` runs with no errors and writes a chart PNG.
- [ ] In the deck, pressing "Run" produces the chart within a reasonable time (a loading message is shown during the Pyodide download).
- [ ] The slider changes the name effect, and the chart changes to match (effect 0 → shelves roughly equal).
- [ ] Exactly 1,000 customers per shelf are simulated. With the same seed, the result is the same every time.
- [ ] Slide 12 says clearly (in Hebrew) that the name effect is an assumption for the demo and not a real finding.
- [ ] The embedded code is identical to `final/simulation.py`.

---

## 8. File Structure

```
ex01-marketing/
├── PRD.md                    # this document
├── README.md                 # project overview + Progress Log + screenshots (updated every push)
├── .gitignore                # includes /docs/l02-summary.pdf (never pushed)
├── docs/
│   ├── concept-brief.md      # shared concept (Hebrew)
│   ├── team-roles.md
│   ├── red-team-review.md    # findings of the external-LLM review + how we fixed them
│   └── l02-summary.pdf       # LOCAL ONLY – git-ignored
├── prompts/
│   ├── 01-project-setup.md
│   ├── 02-team-roles.md
│   ├── 03-prd.md
│   └── NN-<short-name>.md    # every important prompt, numbered, with a short note on the result
├── src/
│   ├── deck-v1.html, deck-v2.html, …   # Raghad – the presentation
│   ├── simulation.py                   # Raghad – Python simulation
│   └── film-v1.html, film-v2.html, …   # Raneem – the 3D film
└── assets/
    └── screenshots/          # screenshots for README (deck slides, film frames, chart)
```

The **latest** `deck-vN.html` embeds the **latest** `film-vN.html` with a relative path (`<iframe src="film-vN.html">`). Both files stay in `src/`.

---

## 9. Work Split and Collaboration Rules

| | Raneem Daher | Raghad Rabah |
|---|---|---|
| Owns | D2 – the film (`src/film-v*.html`) | D1 – the deck (`src/deck-v*.html`), D3 – `src/simulation.py` |
| Shared | PRD, README, prompts, red-team review, final integration check | same |

1. **Before work:** in GitHub Desktop, Fetch origin, then Pull if offered.
2. **Each person edits only her own files.** Shared files (README, PRD) are edited one person at a time, to avoid conflicts.
3. **Versioning:** every significant change goes in a new file (`v1`, `v2`, `v3` …). Earlier versions are kept.
4. **Prompts:** every important prompt is saved in `prompts/NN-<name>.md`, with a short note on what happened. Prompts are kept short and focused, to save tokens.
5. **Push after each working step**, never as one big push at the end. Each commit has:
   - a short title,
   - 2–3 lines: what changed, why, and whether it is **critical** or **minor**.
6. **README on every push:** update the Progress Log (date + what was done) and add or refresh screenshots in `assets/screenshots/` when something visual changed.
7. **Repo access:** both team members + the lecturer are collaborators (lecturer email from Moodle).

---

## 10. Milestones

| # | Milestone | Owner | Done when |
|---|---|---|---|
| M0 | Setup: repo, structure, team roles, concept brief | Both | ✅ done (2026-11-01/02) |
| M1 | PRD v1 approved and pushed | Both | `PRD.md` in repo |
| M2 | Film v1: tube + 5 objects + auras, timeline 15–20 s | Raneem | `film-v1.html` plays end to end |
| M3 | Deck v1: 15 slides with navigation, RTL/BiDi, text + placeholders | Raghad | `deck-v1.html` navigable |
| M4 | Simulation v1: `simulation.py` runs locally + Pyodide Run button in deck | Raghad | chart appears on slide 12 |
| M5 | Film v2: captions + sound + Play/Replay; embedded in deck | Raneem (+ Raghad for embedding) | film plays inside slide 11 |
| M6 | Content pass: verified Rhode facts + sources, final copy, pricing/KPIs | Both | every Rhode claim has a source |
| M7 | Red-team review by a different LLM, fixes as v(N+1) | Both | `docs/red-team-review.md` + fixes pushed |
| M8 | Submission: final README with screenshots, Moodle Word form → PDF with names, IDs and GitHub link | Both | submitted on Moodle |

Each milestone ends with at least one push.

---

## 11. Red-Team Review (before submission)

- Run by a **different LLM** from the one used to build (for example Gemini or ChatGPT if we built with Claude).
- Prompt: act as a critical "panel of experts" (marketing lecturer, UX/RTL specialist, front-end developer, IP/legal reviewer). Review the deck, film and simulation against this PRD.
- Specific checks: Rhode IP rule, factual accuracy of Part A, BiDi errors, honesty of the simulation, slide count, film length, broken buttons.
- The prompt is saved in `prompts/`. The findings and our response (fixed / rejected + reason) go in `docs/red-team-review.md`. Fixes ship as a new version.

---

## 12. Global Definition of Done

- [ ] All acceptance criteria in §5.3, §6.3 and §7.4 are met.
- [ ] Content and IP rules (§4) are met. A final search of the repo finds no Rhode images or logos and no photos of people.
- [ ] `prompts/` contains the full numbered prompt chain.
- [ ] `README.md` explains the project, each part and how to run it. It has an up-to-date Progress Log and screenshots.
- [ ] Git history shows steady, meaningful pushes from both team members.
- [ ] Red-team review is done and documented.
- [ ] Lecturer is added as a collaborator. The Moodle form is submitted as PDF.

---

## 13. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Pyodide is slow to load or needs internet | Loading indicator. Test on the presentation network. Keep a pre-rendered chart PNG as a fallback |
| Browser blocks film audio | Film starts with a Play click (user gesture) |
| BiDi bugs in mixed Hebrew/English | `<bdi>` / `dir="ltr"` for all English; visual check of every slide |
| Inaccurate Rhode facts (LLM hallucination) | Only verified facts with sources; drop anything we cannot verify |
| Merge conflicts | Separate files per owner; shared files edited one at a time; Fetch/Pull before work |
| Scope creep and token cost | Short prompts; stop at "good"; 4–8 hours target |
| CDN unavailable on presentation day | Test beforehand; keep screenshots / a recording of the film as backup |

---

## 14. Open Decisions

- Final slogan and shade names (currently drafts).
- AURA price point (fictional, for example ₪59–₪79) and KPI target numbers.
- Base purchase probability and the default "name effect" value for the simulation.
- Fonts (Heebo or Assistant).
