# 09 – Embed Film v3 in Deck v3

## Prompt

```
The film inside my deck does not work. Please fix it:
1. Check that src/film-v3.html exists. If not, tell me and stop.
2. Find my latest deck file and the slide where the film is embedded (the iframe).
3. Replace the old film with film-v3.html. Make sure the path is correct
   relative to where the deck file is (both files should be in src/;
   if the deck is in the root, move it into src/ first).
4. Make sure the iframe allows sound and fullscreen (allow="autoplay; fullscreen").
5. Save as the next deck version (e.g. deck-v3.html), open it in Chrome,
   and tell me in simple words what was wrong and what you fixed.
Save this prompt in prompts/09-embed-film-v3.md. Do not commit yet.
```

## Result (note)

- Verified `src/film-v3.html` exists in `src/`.
- Moved the deck into `src/` (removed the misplaced root `deck-v1.html`) and saved the new version as `src/deck-v3.html` so both `deck-v3.html` and `film-v3.html` sit side by side in `src/`.
- Updated the `<iframe>` on Slide 10 to `src="film-v3.html"` with `allow="autoplay; fullscreen"` and removed `loading="lazy"` so the Three.js scene initializes immediately even while the slide is hidden.
- Opened `src/deck-v3.html` in Chrome to verify playback.
