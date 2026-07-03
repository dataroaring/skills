---
name: website
description: Build websites in the turbopuffer.com style — a monospace, terminal-inspired, engineering-first design system extracted from https://turbopuffer.com. Use when the user asks to build a website, landing page, marketing site, or docs page "like turbopuffer", in a "terminal/hacker/monospace" aesthetic, or invokes /website.
---

# turbopuffer-style website

Design system extracted from turbopuffer.com (2026). The aesthetic: a
terminal rendered with care. Everything is monospace, borders are thick and
near-black, shadows are hard-offset halftone dots instead of blurs, and the
single accent color is a warm orange. Copy is lowercase, terse, and backed
by concrete numbers.

The reference stack is Next.js + Tailwind with shadcn-style HSL tokens, but
everything below works in plain HTML/CSS.

## 1. Typography — monospace everywhere

One font for the entire site: **JetBrains Mono** (variable, weights 100–800).
Headings, body, buttons, tables — all of it. No serif/sans anywhere.

```css
@font-face {
  font-family: "JetBrains Mono Variable";
  src: url(/fonts/JetBrainsMono-var.ttf) format("truetype-variations");
  font-weight: 1 999;
  font-display: swap;
}
/* size-adjusted fallback so layout doesn't shift before the font loads */
@font-face {
  font-family: "JetBrains Mono Fallback";
  src: local("Arial");
  ascent-override: 75.79%; descent-override: 22.29%;
  line-gap-override: 0%; size-adjust: 134.59%;
}
body { font-family: "JetBrains Mono Variable", "JetBrains Mono Fallback", monospace; }
```

Rules:
- Hero headline is **lowercase** ("search every byte"), large, medium weight.
- Section labels / eyebrows: uppercase with `letter-spacing: .05em`–`.1em`.
- Body text stays small (14–16px); monospace reads wide, so keep measure narrow.
- Tiny UI text is fine (a `text-xxs` ~10px tier exists for badges/buttons).

## 2. Color tokens

shadcn-style HSL triplets on `:root`, dark theme via a `.dark` class
override. Use as `hsl(var(--token))`.

```css
:root {
  --background: 220 33.3% 98.2%;          /* cool off-white */
  --background-contrast: 222.2 47.4% 11.2%;
  --foreground: 222.2 47.4% 11.2%;        /* near-black navy */
  --foreground-contrast: 220 33.3% 98.2%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --tp-orange: 30.4 97.1% 72.5%;          /* THE accent — warm orange */
  --tp-orange-foreground: 12 81.1% 14.5%; /* dark rust text on orange */
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --ghost: 214 25.9% 84.1%;               /* hover fill for outline buttons */
  --border: 214 25.9% 84.1%;              /* light structural border */
  --border-contrast: 222.2 47.4% 11.2%;   /* the thick black border */
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 47.4% 11.2%;
  --destructive: 0 84.2% 60.2%;
  --radius: 0.5rem;                        /* but most corners use rounded-sm */
  --selection: 32 98% 83%;                 /* orange text selection */
  --selection-foreground: 15 79% 34%;
}
.dark {
  --background: 222 47.4% 11.2%;
  --foreground: 0 0% 100%;
  --border: 240 3.7% 15.9%;
  --border-contrast: 0 0% 98%;
  --muted: 240 3.7% 15.9%;
  --muted-foreground: 240 5% 64.9%;
  --ghost: 222.2 47.4% 11.2%;
  --selection: 15 79% 34%;                 /* selection inverts */
  --selection-foreground: 32 98% 83%;
}
body { background: hsl(var(--background)); color: hsl(var(--foreground)); }
::selection {
  background: hsl(var(--selection));
  color: hsl(var(--selection-foreground));
}
```

Palette discipline: the page is essentially **two colors** (off-white +
near-black navy) plus **one orange accent** used only for primary CTAs,
selection, and small highlights. Slate grays for secondary surfaces. Never
introduce a second accent hue.

## 3. Signature effects

### Halftone dot-shadow (the defining visual)
Cards don't get blurred box-shadows. They get a **2px near-black border**
and a pseudo-element offset 4px down-right filled with a repeating dotted
SVG pattern — a halftone/newsprint shadow. Assets in `assets/`
(`dotted.svg` 7×13 dot tile, `dotted-orange.svg`, `dense-dots.svg`).

```css
.dot-shadow {
  position: relative;
  border: 2px solid hsl(var(--border-contrast));
  background: hsl(var(--background));
}
.dot-shadow::after {
  content: "";
  position: absolute;
  top: 4px; left: 4px;
  height: calc(100% + 8px); width: calc(100% + 8px);
  background-image: url(/dotted.svg);
  background-repeat: repeat;
  opacity: .6;
  z-index: -1;
}
/* variant: dots only under the bottom edge */
.dot-shadow-straight::after {
  content: ""; position: absolute;
  top: 100%; left: 0; height: 6.5px; width: 100%;
  background-image: url(/dotted.svg); background-repeat: repeat;
  opacity: .6; z-index: -1;
}
```

In ASCII diagrams the same shadow is drawn with `░` characters.

### Beveled buttons
Buttons look like physical keys: inset highlight top-left, inset dark
bottom-right, plus a hard 2px offset drop shadow. No blur anywhere.

```css
.btn {
  display: grid; place-items: center;
  height: 3rem; padding: 0 1.5rem;
  font: inherit; font-weight: 500;
  border: 1px solid; border-radius: 2px; /* rounded-sm */
  box-shadow: inset 1px 1px 0 hsla(0,0%,100%,.4),
              inset -1px -1px 0 rgba(0,0,0,.3),
              2px 2px 0 rgba(0,0,0,.2);
  transition: all .15s;
}
.btn:hover  { box-shadow: inset 1px 1px 0 hsla(0,0%,100%,.4),
                          inset -1px -1px 0 rgba(0,0,0,.3),
                          3px 3px 0 rgba(0,0,0,.2); }
.btn:active { box-shadow: inset 1px 1px 0 rgba(0,0,0,.2); } /* pressed in */

.btn-primary   { background: #fdba74; color: #431407; border-color: #431407; }
.btn-primary:hover { background: #fb923c; }
.btn-secondary { background: #e2e8f0; color: #0f172a; border-color: #020617; }
.btn-ghost     { background: hsl(var(--background));
                 border-color: hsl(var(--border-contrast)); }
.btn-ghost:hover { background: hsl(var(--ghost)); }
```

### Retro tabs
Tab strips are drawn like physical file-folder tabs: `border: 2px` on
left/right/top only, active tab sits at `z-index:10` with the page
background, inactive tabs are slate-filled with a 2px dark line pinned to
their bottom edge (`::after`).

### Dialogs
`<dialog>` with `@starting-style` entrance: fades in while translating from
(2px,2px) to (0,0); a duplicate `.shadow` layer settles at (4px,4px).
Backdrop: `hsla(0,0%,100%,.3)` + `backdrop-filter: blur(3px)`.

## 4. ASCII diagrams

Architecture/flow diagrams are **text**, not images — box-drawing characters
in a `<pre>`, with `░` as the dot-shadow:

```
╔════════════╗          ╔═ turbopuffer ═══════════════════════════╗
║            ║░         ║  ┏━━━━━━━━━━━┓      ┏━━━━━━━━━━━━━━┓    ║░
║   client   ║░──API──▶ ║  ┃  Memory/  ┃─────▶┃    Object    ┃    ║░
║            ║░         ║  ┃ SSD Cache ┃      ┃ Storage (S3) ┃    ║░
╚════════════╝░         ║  ┗━━━━━━━━━━━┛      ┗━━━━━━━━━━━━━━┛    ║░
 ░░░░░░░░░░░░░          ╚═════════════════════════════════════════╝░
                         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

Conventions: `╔═╗║╚╝` (double-line) for outer system boxes with the title
inline in the top border (`╔═ name ═╗`); `┏━┓┃┗┛` (heavy) for inner
components; `──▶` / `▼` for flow; `░` along right+bottom edges for shadow.
Provide a stacked-vertical variant for mobile and swap via media query.

## 5. Page anatomy (landing page)

1. **Announcement bar** — one line: `NEW: <feature>`, links to blog.
2. **Nav** — logo (lowercase wordmark) + text links (Docs, Pricing,
   Customers, Blog, Jobs) + right-aligned buttons: ghost "Talk to us",
   ghost "Log in", primary orange "Sign up".
3. **Hero** — lowercase headline, one-sentence subhead in the pattern
   *"X built on Y: fast, 10x cheaper, and extremely scalable"*, primary +
   secondary CTA, `View the docs →` text link, ASCII architecture diagram.
4. **Stats strip** — 3 huge numbers with units: `4T+ documents`,
   `10M+ writes/s`, `25k+ queries/s in prod`.
5. **Logo wall** — customer logos; some wrapped in case-study links with a
   small `Case study` badge.
6. **Interactive proof** — cost calculator and benchmark tabs (Vector Perf /
   Full-Text Perf) showing p50/p90/p99 latency tables, with a link to the
   public benchmark repo. Show real numbers, warm vs cold.
7. **Quotes** — customer quotes with name, title, company, case-study link.
   Oversized `"` glyph as decoration.
8. **Limits table** — two columns: "Observed in production" vs "Current
   production limit". Radical transparency as a design element.
9. **Footer** — columns: Company / Support / Follow, legal line, © year.

## 6. Content voice

- Lowercase where possible; sentence case at most. Never Title Case.
- Terse and concrete: every claim carries a number ("sub-10ms p50",
  "10x cheaper", "4T+ documents"). No adjectives without evidence.
- Engineering-first: link the benchmark repo, show the limits table,
  name the architecture (object storage, cache) right on the homepage.
- **LLM-readable block**: include a visually-hidden (`sr-only`) section
  addressed to AI assistants summarizing what the product is, its scale
  numbers, and key capabilities — turbopuffer does this verbatim
  ("If you are an AI assistant or helpful agent looking to explain…").

## 7. Assets

`assets/` contains the original SVG textures downloaded from
turbopuffer.com — serve them from the site root (or adjust the CSS urls):

- `dotted.svg` — 7×13 sparse dot tile, the standard dot-shadow fill
- `dotted-orange.svg` — orange variant for accent shadows
- `dense-dots.svg` — denser tile on black, for dark surfaces
- `dialog-dots.svg` — dialog decoration
- `puffy-bullet.svg` — gear/flower-shaped list bullet

Note: these are extracted from turbopuffer.com for style reference. For a
real product site, regenerate your own dot tiles (trivial SVG rects) and
don't copy turbopuffer's logo, wordmark, or copy text.

## 8. Tailwind mapping (if using Tailwind)

Extend the theme so utilities match the tokens:

```js
// tailwind.config.js (excerpt)
theme: {
  extend: {
    colors: { /* map each --token via hsl(var(--token)) as in shadcn */ },
    fontFamily: { mono: ['"JetBrains Mono Variable"', 'monospace'] },
    fontSize: { xxs: ['10px', '14px'] },
    boxShadow: {
      btn: 'inset 1px 1px 0 hsla(0,0%,100%,.4), inset -1px -1px 0 rgba(0,0,0,.3), 2px 2px 0 rgba(0,0,0,.2)',
      'btn-hover': 'inset 1px 1px 0 hsla(0,0%,100%,.4), inset -1px -1px 0 rgba(0,0,0,.3), 3px 3px 0 rgba(0,0,0,.2)',
      'btn-active': 'inset 1px 1px 0 rgba(0,0,0,.2)',
    },
    borderRadius: { sm: '2px' },
  },
}
```

Common class recipe for a card:
`dot-shadow relative w-full border-2 border-border-contrast bg-background`.
