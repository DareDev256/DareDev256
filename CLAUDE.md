# CLAUDE.md — DareDev256 Profile README

## #1 Rule: README Size Cap

**README.md must stay under 120 visible lines and ~300 total lines.** This is non-negotiable.

- Only write inside auto-update marker zones (`DAILY_STATUS_START/END`, `SHOWCASE_SECTION_START/END`)
- Showcase updates: **1-2 lines max** — project name, one sentence, diff stats, live link
- New content goes inside existing `<details>` blocks, NOT as new visible sections
- Never add ASCII art, timeline blocks, tables, or multi-line code blocks outside `<details>`
- Never expand collapsed sections into visible content
- New projects → add to the collapsed "Everything else" block

## Structure (do not change)

Visible sections in order: Hero → Featured → Hackathons → Also Worth a Look → Open To → Footer

Collapsed sections: AI literacy games, Everything else, Hard problems I've actually solved, What I'd build differently

## Link Rule (v0.9.0 — non-negotiable)

**Never link a private repo.** A `github.com/DareDev256/<private-repo>` link renders as a
404 to every visitor — the profile's own credibility surface, broken. Before adding any
repo link, verify it is public:

```bash
gh api repos/DareDev256/<repo> --jq '.private'   # must print: false
```

For private work with a public deployment (e.g. second-opinion), link the **live demo
only** and name the project in bold without a repo link. v0.9.0 removed 8 such dead links.

## Metrics Rule (v0.9.0 — non-negotiable)

**No hardcoded counts.** Star totals, fork counts, repo counts, and commit counts drift
silently and make the profile lie. Use Shields.io dynamic endpoints, which read live:

```
https://img.shields.io/github/stars/DareDev256/<repo>?style=flat-square
https://img.shields.io/github/forks/DareDev256/<repo>?style=flat-square
```

Any claim with a number in it must be verifiable from a live source or cut. v0.9.0 removed
the hardcoded `Stars-71` (real: 99), `44 stars` (real: 68), `⭐7` (real: 8), `Commits_2026-770`,
`35 public repos` (real: 32), and several unverifiable ecosystem stats.

## Auto-Update Zones

Two marker-delimited zones that Passion Agent can write to:
- `<!-- DAILY_STATUS_START -->` ... `<!-- DAILY_STATUS_END -->` — daily task stats
- `<!-- SHOWCASE_SECTION_START -->` ... `<!-- SHOWCASE_SECTION_END -->` — latest notable build

Everything outside these markers requires human review.

## Versioning

- CHANGELOG.md follows Keep a Changelog format
- Semantic versioning: major = full redesign, minor = new sections, patch = updates
- Current: v0.9.1

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
- Subtitle text = brand identity titles (AI SOLUTIONS ENGINEER, CREATIVE TECHNOLOGIST, AUTONOMOUS AGENT BUILDER, MUSIC VIDEO DIRECTOR). These are **not** the same as Open To job targets — subtitles describe what James *is*, Open To lists what he's *seeking*. Do not "sync" these.
- Tagline stats ("47 REPOS", "24/7 AI ECOSYSTEM") must match badge and bio numbers (see FOR_DARE.md Metrics Sync Map)
- No external dependencies — the SVG is fully self-contained by design (replaced `readme-typing-svg`)

## See Also

- `FOR_DARE.md` — detailed project documentation, troubleshooting, badge services
