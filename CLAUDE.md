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

Collapsed sections: How the Passion Ecosystem Works, All 33 Projects, Hard Problems I've Solved, What I'd Build Differently

## Auto-Update Zones

Two marker-delimited zones that Passion Agent can write to:
- `<!-- DAILY_STATUS_START -->` ... `<!-- DAILY_STATUS_END -->` — daily task stats
- `<!-- SHOWCASE_SECTION_START -->` ... `<!-- SHOWCASE_SECTION_END -->` — latest notable build

Everything outside these markers requires human review.

## Versioning

- CHANGELOG.md follows Keep a Changelog format
- Semantic versioning: major = full redesign, minor = new sections, patch = updates
- Current: v0.7.0

## See Also

- `FOR_DARE.md` — detailed project documentation, troubleshooting, badge services
