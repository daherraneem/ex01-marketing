# 06 – Film v2 (five tubes, natural look)

## Prompt

```
Create src/film-v2.html by copying film-v1.html and editing only what is needed:
1. Concept change: each lip tint has its own flavor. Replace the single tube
   with 5 tubes, one per shade, each shown together with its own food
   (Honey Glaze + honey, Peach Nectar + peach, Berry Juice + berries,
   Pomegranate Drop + pomegranate, Cocoa Kiss + cocoa bean). No mixing into one tube.
2. More natural look: realistic glossy/juicy materials, soft lighting with shadows,
   tubes that look like real cosmetic packaging. Keep everything built from 3D objects.
3. Keep it 15-20 seconds, keep the sound, captions and Play button.
   End card: all 5 tubes together + AURA logo + slogan.
Also update the storyboard in docs/concept-brief.md (section 6) to match.
Save this prompt in prompts/06-film-v2.md.
Open the film in Chrome when done. Do not commit yet.
```

## Result (note)

- `src/film-v2.html` – still 20 s. It keeps v1's player: Play/Replay, Web Audio sound, RTL captions, the orbit-camera button and the `?t=` frame preview. The scene is new.
- **Five tubes in a row**, each a real-looking package: a thick clear glass bottle (physical transmission and refraction), tinted liquid in the shade color, a printed "AURA + shade name" label, a gold cap with a band in the shade color, and a wand with a doe-foot applicator.
- **Five 2-second "flavor moments" (3–13 s):** the camera moves from pair to pair. Each food floats down beside its own tube, its aura blooms, and a label shows the shade name and flavor (e.g. "Honey Glaze · בטעם דבש"). One chime per shade.
- **13–16 s:** the five caps pop open one after another, and each applicator draws a swatch in its own shade, with sparkles.
- **16–20 s:** end card with all five tubes and their foods, the AURA logo, the slogan and "הזוהר שלך מתחיל כאן".
- **Natural look:** soft shadows on a matte floor, lights that come up at the start, see-through honey and pomegranate seeds, fuzzy peach skin, less bloom than v1.
- `docs/concept-brief.md` §6 – storyboard rewritten for v2, with a note on what changed from v1.
- Fixes during the build (checked with headless screenshots): the floor looked grey and shiny, so it is now a dark matte surface. The camera was too close in the flavor moments. The shade label moved above the food so it does not cover the caption. The aura glow had a hard edge where the floor cut it.
