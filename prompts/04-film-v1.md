# 04 – Film v1 (3D ad)

## Prompt

```
Read PRD.md (the 3D film section) and docs/concept-brief.md (section 6, storyboard).
Build the AURA 3D ad, version 1:
- Three.js, one HTML file: src/film-v1.html
- 15-20 seconds, following the storyboard
- A Play button to start (film + sound)
- Sound effects made with the Web Audio API (no audio files)
- Hebrew captions, RTL
- All visuals original, built from 3D objects
Save this prompt in prompts/04-film-v1.md.
When done, open the file in Chrome so I can check it. Do not commit yet.
```

## Result (note)

- `src/film-v1.html` – a 20-second film with Three.js (CDN, ES modules) and bloom post-processing.
- Built only from geometry: a glass tube with a gold cap, a wand and an applicator. The five foods are a honey drop, a peach, berries, a pomegranate with seeds and cocoa beans. Each food has an aura in its exact shade HEX.
- Timeline follows PRD §6.2: the tube appears (0–3 s), the foods float in with chimes and shade labels (3–8 s), the auras swirl into the tube and fill it in 5 colored layers (8–13 s), the cap opens and draws a juicy gradient line with sparkles (13–16 s), then the AURA logo, the slogan and "הזוהר שלך מתחיל כאן" (16–20 s).
- Sound: Web Audio only. Opening pad, a chime per food, a panning whoosh, "plops", a cap pop, sparkle and a closing chord.
- Play button → Replay + optional free-orbit camera at the end. Fills any iframe size.
- Dev aid: `film-v1.html?t=14.5` freezes the film at that second, with no sound, for screenshots.
- Fixes made during the build (checked with headless screenshots): the tube fill looked washed out, so the glass and glow were toned down. The Cocoa Kiss label covered the cap, so it moved above the bean. The camera now frames the cap during the line drawing.
