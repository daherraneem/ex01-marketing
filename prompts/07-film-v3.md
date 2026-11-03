# 07 – Film v3 (Raghad's shades, deck style, one moment per shade)

## Prompt

```
Create src/film-v3.html from film-v2.html (edit, don't rebuild). Make it fancy and professional:
1. Use exactly Raghad's shades from deck-v1.html (names, colors, foods).
   Show each shade alone, one after another, ~3.5 seconds each: its tube + its food.
2. Match her deck style: light cream-peach background with blurred glowing aura circles,
   background color changing per shade, her fonts (Cormorant Garamond + Assistant).
3. More realistic: real glass with reflections (environment lighting), soft shadows,
   metallic gold bands, glossy juicy foods. Still built from 3D objects only.
4. Soundtrack (Web Audio, no audio files): a fresh, upbeat track for the whole film,
   with a short musical signature for each shade.
5. Intro 2s + 5 shades + end card (all 5 tubes, AURA logo, slogan). Total 20-25 seconds.
   Keep the Play button and Hebrew captions (RTL).
6. Update the shade names in PRD.md and docs/concept-brief.md to Raghad's names.
Check frames yourself and fix problems before showing me.
Save this prompt in prompts/07-film-v3.md. Open the film in Chrome. Do not commit yet.
```

## Result (note)

- `src/film-v3.html` – 24 s. It keeps v2's player: Play/Replay, Web Audio, RTL captions, the orbit-camera button and the `?t=` frame preview.
- **Raghad's five shades**, with names, colors and foods taken from `deck-v1.html`: Golden Honey Glaze (honey dipper and a honey drop), Velvet Peach Nectar (peach and blossom), Berry Crush Elixir (strawberry and blueberries), Ruby Pomegranate Jewel (pomegranate and seeds), Silk Cocoa Glaze (chocolate, cocoa bean and coffee bean).
- **One shade at a time, 3.5 s each:** every shade has its own podium, tube and food, far apart so each is alone in the frame. The camera pans from one to the next. In each moment the food drops onto its podium, a glow blooms behind it, the cap pops and a glossy ribbon in the shade color swirls around the tube. A card in the deck's style shows the badge ("גוון 01 • בטעם דבש"), the Hebrew name, the English name and a color bar.
- **Deck style:** the same cream-peach radial gradient and two blurred aura circles as the deck, with colors that change to each shade's deck colors. Fonts are Cormorant Garamond for the brand and Assistant for Hebrew. The tube copies her design: a pearl cap tinted per shade, a gold collar, a liquid gradient from light to dark, a vertical "AURA" label and a pill with the number and name.
- **Realism:** environment lighting (reflections on glass, gold and gloss), clear glass with refraction, soft shadows on an invisible floor, neutral tone mapping so the deck colors stay true.
- **Soundtrack:** 137 BPM, so one bar = 1.75 s and every shade is exactly 2 bars. It has a pop groove in D major (kick, clap, hats, bass, chord stabs) and a signature per shade: honey = marimba, peach = flute, berry = bright plucks, pomegranate = glass bells, cocoa = soft e-piano. The end card has a bell "AURA" motif.
- **Timeline:** intro 0–1.75 s (one music bar, close to the 2 s asked), shades 1.75–19.25 s, end card 19.25–24 s.
- `PRD.md` and `docs/concept-brief.md`: the shade tables and all shade names now use Raghad's names and colors.
- Fixes during the build (checked with headless screenshots): the lifted cap went out of the frame, so the swatch became a ribbon around the tube. The first tube showed during the intro. The end-card halo was visible during the cocoa shade. The gold looked dark brown. The liquids looked washed out. The pomegranate sank into its podium when it landed.
