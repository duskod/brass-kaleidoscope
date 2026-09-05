# Brass Kaleidoscope

A kaleidoscope you can point at the light. **https://kaleidoscope.clockerly.com**

Not a symmetry filter: it simulates the instrument. Coloured glass sits in a backlit object
cell with a small granular-physics engine, and two front-surface mirrors reflect the wedge
between them around the apex. Turn the tube and the glass tumbles; no pattern ever comes back.

## On a phone
- **Turn the phone** and gravity swings round the cell, just like turning a real tube.
- **Shake it** to shake the glass. Lay it flat and the glass barely moves, as when a scope
  is pointed at the sky.
- **Light** comes from the back camera used as a light meter: point it at a lamp and the
  glass blazes; point it at the floor and it goes dim.
- **Teleidoscope**: switch *Object* to *Camera* and the mirrors reflect the live camera image.
  Pinch the eyepiece, or use the Lens slider, to zoom.
- **Snapshot** renders the pattern at your screen's resolution and opens the share sheet,
  so "Set as wallpaper" is a tap away.
- Install it from the browser menu ("Add to Home screen"); it works offline.

## On a desktop
Drag the eyepiece to turn, scroll to fine-turn, `←`/`→` turn, `space` shakes, `f` fullscreen,
`s`/`S` snapshot (fill / fit). Light is a slider.

## Controls
Mirror angle (60° → 6-fold … 22½° → 16-fold), fifteen glass sets plus a custom editor with
a "Roll" that generates harmonious sets, dry or oil-filled cell, number of pieces, clockwork
turn.

## Files
| file | what |
|---|---|
| `index.html` | the whole app, one file, no build step, no dependencies beyond two Google Fonts |
| `manifest.webmanifest`, `sw.js`, `icon-*.png` | installable-app packaging and offline shell |
| `src-artifact.html` | the same page without the document wrapper, as authored in Claude Code |
| `build.py` | wraps `src-artifact.html` into `index.html` (run after editing the source) |
| `icon.svg` | the app icon; the PNGs are rendered from it |

## Physics notes
Circles with a friction impulse model, three contact iterations per 1/240 s substep. Piles
settle because a piece is held when no downhill direction is free of all its contacts
(with a friction cone), and held pieces skip gravity and are immovable to slow neighbours.
Rendering avoids canvas `filter` (software on Android): saturation is baked into the glass
colours, the mirror wedge is clipped once and stamped, and bloom is a shrink-and-stretch.

Built in one evening with Claude Code. MIT licence.
