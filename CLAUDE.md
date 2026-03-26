# CLAUDE.md — DareDev256 Profile README

## #1 Rule: README Size Cap

**README.md must stay under 120 visible lines and ~300 total lines.** This is non-negotiable.

- Only write inside auto-update marker zones (`DAILY_STATUS_START/END`, `SHOWCASE_SECTION_START/END`)
- Showcase updates: **1-2 lines max** — project name, one sentence, diff stats, live link
- New content goes inside existing `<details>` blocks, NOT as new visible sections
- Never add ASCII art, timeline blocks, tables, or multi-line code blocks outside `<details>`
- Never expand collapsed sections into visible content
- New projects → add to collapsed "All 33 Projects" block, update count

## Structure (do not change)

Visible sections in order: Hero → Currently Building → Featured Projects → Open To → Tech Stack → Proof of Craft → GitHub Stats → Footer

Collapsed sections: Domain Depth + Technical DNA, How the Passion Ecosystem Works, All 33 Projects, Hard Problems I've Solved, What I'd Build Differently, Repo Setup & Dependencies

## Auto-Update Zones

Two marker-delimited zones that Passion Agent can write to:
- `<!-- DAILY_STATUS_START -->` ... `<!-- DAILY_STATUS_END -->` — daily task stats
- `<!-- SHOWCASE_SECTION_START -->` ... `<!-- SHOWCASE_SECTION_END -->` — latest notable build

Everything outside these markers requires human review.

## Versioning

- CHANGELOG.md follows Keep a Changelog format
- Semantic versioning: major = full redesign, minor = new sections, patch = updates
- Current: v0.8.19

## Assets

### `signature.svg` — Animated Hero Emblem

| Property | Value |
|----------|-------|
| **Type** | Inline SVG with CSS-only animations (no JavaScript) |
| **Dimensions** | 800 × 250 (`viewBox="0 0 800 250"`) — displayed at `width="600"` in README |
| **Color palette** | `#6C63FF` (primary), `#A78BFA` (secondary), `#818CF8` (tertiary) |
| **Theme support** | `prefers-color-scheme: light` swaps text fills — emblem colors stay constant |
| **Animations** | Draw-in (infinity path), orbital rotation, spoke reveal, cycling subtitles (4 titles, 12s loop) |
| **Referenced in** | `README.md` line 7 (`<img src="./signature.svg">`) — hero image, above the fold |

**Constraints:**
- Color values must stay in sync with Shields.io badge `color=6C63FF` used throughout README
- Subtitle text ("AI SOLUTIONS ENGINEER", etc.) must match role titles in Open To section
- Tagline stats ("47 REPOS", "24/7 AI ECOSYSTEM") must match badge and bio numbers
- No external dependencies — the SVG is fully self-contained by design (replaced `readme-typing-svg`)

## See Also

- `FOR_DARE.md` — detailed project documentation, troubleshooting, badge services
