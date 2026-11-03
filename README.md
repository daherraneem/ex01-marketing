# ex01-marketing

## Final Submission

**Final files:**

| Deliverable | File |
| ----------- | ---- |
| Presentation (final deck) | [`final/deck.html`](final/deck.html) |
| 3D launch film | [`final/film.html`](final/film.html) |
| Python simulation | [`final/simulation.py`](final/simulation.py) |

**How to view:**

1. Download the repository (Code → Download ZIP) or clone it: `git clone https://github.com/daherraneem/ex01-marketing.git`
2. Open [`final/deck.html`](final/deck.html) in Chrome. The film is on Slide 10 and the Python simulation is on Slide 11.
3. An internet connection is needed: the Python simulation runs in the browser with Pyodide, which loads from the internet (so do the fonts and Three.js).
4. The film starts with the Play button (▶ הפעל). Turn the sound on.

[`archive/`](archive/) keeps our earlier versions to show the development process.

---

**Course:** AI Agents & Vibe Coding
**University:** University of Haifa
**Assignment:** Exercise 1
**Team:** Raneem Daher & Raghad Rabah
**Status:** Film final (v3) · Deck final (v4)

## Project Structure

| Folder                | Purpose                                      |
| --------------------- | -------------------------------------------- |
| `prompts/`            | Prompts used with the AI agent, one per step |
| `final/`              | The final submission: deck, film, simulation |
| `archive/`            | Earlier deck and film versions               |
| `assets/screenshots/` | Screenshots for documentation                |
| `docs/`               | Project documentation                        |
| `PRD.md`              | Product Requirements Document (the plan)     |

## Progress Log

- **2026-11-01** – Project setup: created folder structure (`prompts/`, `src/`, `assets/screenshots/`, `docs/`), saved the setup prompt, and wrote the README intro.
- 2026-11-02 – Added team roles document (Raghad).
- **2026-11-02** – Wrote PRD v1 (`PRD.md`): goals, scope, IP rules, deliverables with acceptance criteria, file structure, work split, milestones; added concept brief to `docs/`; git-ignored the lecture summary PDF (Raneem).
- **2026-11-02** – Film v1 (`src/film-v1.html`): 20-second Three.js ad that follows the storyboard. It has the AURA tube, five foods with auras in their shade colors, Hebrew RTL captions, Web Audio sound effects and Play/Replay buttons. All visuals are built from 3D geometry. Prompt saved in `prompts/04-film-v1.md` (Raneem).
- **2026-11-03** – Film v2 (`src/film-v2.html`): 5 tubes, one per shade, each with its own food, and a more natural look. Updated the storyboard in `docs/concept-brief.md` to match. Not selected, because all tubes appear together; next version will give each shade its own moment. Prompt saved in `prompts/06-film-v2.md` (Raneem).
- **2026-11-03** – Film v3 (`src/film-v3.html`), **the final film**: 24 s, Raghad's five shades from the deck, each alone with its own food, the deck's colors and fonts, realistic glass and gold, and a Web Audio soundtrack with a signature per shade. Updated the shade names in `PRD.md` and `docs/concept-brief.md` to Raghad's names. Prompt saved in `prompts/07-film-v3.md` (Raneem).
- **2026-11-03** – Deck v1 → v3 (`src/deck-v3.html`) & Python simulation (`src/simulation.py`): built the Hebrew RTL presentation with 6D floating product slides and campaign slides, added the 1,000-customer A/B Python simulation running in the browser with Pyodide on Slide 11, and embedded the final 3D launch film (`src/film-v3.html`) on Slide 10 with audio and fullscreen support. Prompts saved in `prompts/11-python-simulation.md` and `prompts/09-embed-film-v3.md` (Raghad).
- **2026-11-03** – Deck v4 (`src/deck-v4.html`): updated Slide 7 by removing the content about Hailey Bieber and replacing it with a bridge slide ("מההשראה למותג שלנו") connecting Rhode's food-inspired marketing insight to our original brand, AURA. Prompt saved in `prompts/10-slide7-update.md` (Raghad).
- **2026-11-03** – Prepared the repo for submission: added the "Final Submission" section at the top of the README (final files, how to view), checked that the final deck (`src/deck-v4.html`) embeds `film-v3.html` on Slide 10 and runs the Python simulation on Slide 11, and tagged the commit `submission-ex01` (Raneem).
- **2026-11-03** – Final fixes: film length in `PRD.md` changed to 20–25 s (the final film is 24 s); renamed the duplicate prompt `06-python-simulation.md` to `11-python-simulation.md`; changed "Honey Glaze" to "Golden Honey Glaze" on Slide 11 of `src/deck-v4.html` and in `src/simulation.py` (Raneem).
- **2026-11-03** – Organized the repo with `git mv` (history kept): the final files are now in `final/` (`deck.html`, `film.html`, `simulation.py`) and the earlier deck and film versions are in `archive/`. Updated the film and simulation paths in `final/deck.html`, pointed the archived decks to `../final/film.html`, and updated the README (Raneem).
- **2026-11-03** – Fixes after the red team review (`docs/red-team-review.md`): simulation slider, a believable labelled assumption, Hebrew chart order and an honest "completed" message (slide 11); unsourced percentages removed (slides 6–8) and 3 sourced Rhode facts added (slide 7); Raghad's shade names on slide 8 and the real film length (24 s) on slide 10; parallax only on the product, bigger navigation dots, a non-sticky texture line and warmer sensory words. Updated `PRD.md` (Part A = one bridge slide; simulation model). Saved the committee prompt in `prompts/12-red-team.md` (Raneem).

## Red Team Review

We asked Gemini to review the project as a committee of 10 experts (prompt: [`prompts/12-red-team.md`](prompts/12-red-team.md), full review: [`docs/red-team-review.md`](docs/red-team-review.md)). It gave 62/100. We checked every point against the code and the PRD before acting on it.

**What the committee found (and was right about):**
- The Python simulation had no slider, its 15% vs 45% result (a 3× lift) was not believable, and the Hebrew in the chart was broken. We also found that the slide said "completed" before Python had even run.
- Part A about Rhode was much shorter than the PRD planned, and slides 6–8 showed percentages (94%, 96%, 100%…) with no source.
- The mouse parallax tilted the whole slide, including the text, and the navigation dots were only 12px.
- The copy did not say anything about texture, and the sensory words were weak.

**What we fixed:**
- **Simulation (slide 11):** a slider for the name effect (0–30%), a modest default (10% → 12%, a 20% relative lift) that is labelled as an assumption, Hebrew in the correct right-to-left order, and "completed" only after Python really finishes. `simulation.py` now also runs on a computer and saves a PNG.
- **Slides 6–8:** removed the unsourced percentages (slides 6, 7 and 8). Slide 7 now has 3 short facts about Rhode's food-inspired marketing, each with a public source (Glossy, NewBeauty). The PRD now says Part A is one bridge slide, because we chose to focus on our own brand, AURA.
- **Deck UX:** the parallax moves only the 3D product, never the text; navigation dots are bigger, with a 36 × 44px click area.
- **Copy:** a "melting, silky, non-sticky" texture line in the positioning statement, and warmer sensory words in the five shade descriptions.
- **Consistency:** slide 8 now uses Raghad's shade names (Golden Honey Glaze … Silk Cocoa Glaze), and slide 10 gives the real film length (24 seconds).

**What we chose not to fix, and why:**
- **Replace the serif font, gold and "Jewel" names:** this is the brand identity from Raghad's deck, and the film was built to match it. The cream-honey palette is warm, not "cold luxury".
- **Replace the music with ASMR sounds:** an upbeat track fits a Gen Z social-media ad.
- **Replace the 3D foods with displacement-mapped meshes:** the PRD requires everything to be built from 3D geometry, with no image textures. The glass already refracts the liquid.
- **"Hebrew will show as empty squares":** not true. We tested it: the letters appeared, but in reverse order. We fixed the order; no new font was needed.
- **numpy instead of a Python loop:** 2,000 random draws take milliseconds; loading Pyodide takes about 20 seconds, so this changes nothing.
- **"You promised 15 slides":** the PRD says *up to* 15 slides; the final deck has 12.
- **Lower the price to 39 NIS:** a judgment call. We kept 69 NIS as a fictional target price.

## Film Versions

| Version | File | What it is | Why we changed it | Status |
| ------- | ---- | ---------- | ----------------- | ------ |
| v1 | `archive/film-v1.html` | First version – one AURA tube; the auras of all the flavors flow into it and fill it with color. | – (starting point) | Replaced by v2 |
| v2 | `archive/film-v2.html` | 5 tubes, each with its own flavor and food, and a more natural look (glossy materials, soft light and shadows, realistic cosmetic packaging). | To match our concept that every lip tint has its own flavor, like in Raghad's deck. | **Not selected** – all tubes appear together; we want each shade to have its own moment. |
| v3 | `final/film.html` (was `film-v3.html`) | Each shade alone with its own food (3.5 s per shade), Raghad's exact shades (names, colors, foods) and deck style (cream-peach background with aura circles, her fonts), a more realistic look (glass with reflections, soft shadows, gold collars, glossy foods) and a soundtrack with a musical signature for each shade. | So every lip tint gets its own moment, and the film and the deck look like one campaign. | **Selected – final version** |

## Deck Versions

| Version | File | What it is | Why we changed it | Status |
| ------- | ---- | ---------- | ----------------- | ------ |
| v1 | `archive/deck-v1.html` | First presentation – 5 interactive 6D floating lip tint shade slides in Hebrew RTL with ambient audio and sensory specs. | – (starting point) | Replaced by v2 |
| v2 | `archive/deck-v2.html` | Added the Rhode case study & AURA campaign strategy slides plus Slide 11 with the live Python A/B simulation (`src/simulation.py`) running in the browser via Pyodide. | To back our sensory marketing insight with a 1,000-customer simulation chart directly inside the deck, as required by the PRD. | Replaced by v3 |
| v3 | `archive/deck-v3.html` | Moved the deck into `src/` alongside `film-v3.html` and embedded the final 3D launch film (`src/film-v3.html`) on Slide 10 using an `<iframe>` with `allow="autoplay; fullscreen"`. | Because the old relative path pointed to the wrong folder and lacked audio/fullscreen permissions; placing both files in `src/` makes the embedded 3D film play seamlessly inside Slide 10. | Replaced by v4 |
| v4 | `final/deck.html` (was `deck-v4.html`) | Slide 7: removed the content about Hailey Bieber and replaced it with a bridge slide (from inspiration to our own brand). | Our project focuses on our original brand, AURA; Rhode is used only as inspiration. | **Selected – final version** |

## Screenshots

**Deck preview** – Slide 1 (Golden Honey Glaze) with 6D floating lip tint tube and Hebrew RTL layout:

![Deck preview – Golden Honey Glaze slide](assets/screenshots/deck-preview.png)

**Deck Slide 10 (Embedded 3D Film)** – the film (`final/film.html`, then `film-v3.html`) playing inside Slide 10 of deck v3 (now `archive/deck-v3.html`):

![Deck Slide 10 – embedded 3D launch film](assets/screenshots/deck-slide10-film.png)

**Deck Slide 11 (Python Simulation)** – after clicking "הרץ סימולציה", showing the 1,000-customer A/B test chart (Shelf A numbered names vs. Shelf B AURA food names):

![Deck Slide 11 – Python simulation chart](assets/screenshots/deck-slide11-python.png)

**Film v1** – the five foods, each with an aura in its shade color (at 8 s):

![Film v1 – five foods with their auras](assets/screenshots/film-v1.png)

**Film v3 (final)** – the end card: all five shades with their foods, the AURA logo and the slogan (at 22.5 s):

![Film v3 – end card with the five AURA shades](assets/screenshots/film-v3.png)
