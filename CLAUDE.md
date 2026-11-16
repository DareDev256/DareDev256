# CLAUDE.md — DareDev256 Profile README

## #1 Rule: README Size Cap

**README.md must stay under 120 visible lines and ~300 total lines.** This is non-negotiable.

- Only write inside the auto-update marker zone (`DAILY_STATUS_START/END`), and only from `.github/scripts/build_readme.py`
- New content goes inside existing `<details>` blocks, NOT as new visible sections
- Never add ASCII art, timeline blocks, tables, or multi-line code blocks outside `<details>`
- Never expand collapsed sections into visible content
- New projects → add to the collapsed "Everything else" block

## Structure (do not change)

Visible sections in order (v2.1.0): Hero (signature, hook line, studio shot; its caption names portfolio-os as the source) → Tools (fcp-mcp-server, frameio-to-final-cut-pro / Cut Review, More tools: a 3-up shot row + one bullet each for the prompt generator, clickfix-protection-macos, jackpoint) → Client work (COLD OPEN six-site grid) → Currently → Hackathons (list + One Lesson GIF; no face footage of James) → Open To → Footer

Collapsed sections: Passionate Learning, The six artists behind COLD OPEN (and the blind A/B note), Other projects, Seven bugs with receipts, What I would build differently

Why Tools leads (v2.1.0, 2026-11-15): the GitHub traffic API showed visitors land on the tools (fcp-mcp-server 929 uniques in 14 days, Cut Review 23 and 205 PyPI downloads in week one, prompt generator 13).

Referrer `aocr.org` is NOT an audience (checked 2026-11-15): it is the American Osteopathic College of Radiology, its site links to no GitHub page, and every hit it "sent" is exactly 1 view per visitor on commit pages, workflow folders, CLAUDE.md and pre-rename repo names. Treat it as a bot with a forged referrer; subtract it before calling any repo popular (it was all 17 of clickfix's visitors). Tools people install go above client work. Re-read traffic before reordering: `gh api repos/DareDev256/<repo>/traffic/views`.

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

## Auto-Update Zone

One marker-delimited zone, written only by `.github/workflows/build-readme.yml`:
- `<!-- DAILY_STATUS_START -->` ... `<!-- DAILY_STATUS_END -->` — latest release, latest
  commit, and live CI conclusion, each clickable, plus the date it was generated.

The SHOWCASE_SECTION zone was removed on 2026-08-31. CHANGELOG shows Passion Agent used to
write it, but it is empty in every README commit in this checkout, and no writer in this
repo emits it: `build_readme.py` writes DAILY_STATUS and nothing else. An advertised
auto-update zone that renders blank costs more credibility than no zone at all. Do not
re-add a marker zone without a committed writer for it.

Everything outside the remaining markers requires human review.

## Versioning

- CHANGELOG.md follows Keep a Changelog format
- Semantic versioning: major = full redesign, minor = new sections, patch = updates
- Current: v2.1.0

## Assets

### Screenshot Rule (v2.0.0)

`assets/studio.jpg`, `assets/sites/*.jpg` and `assets/tools/*.jpg` are photographs of live sites or of the tool repos' own dated screenshots (cropped 2:1), so every
caption under them carries its shot date (`Shot YYYY-MM-DD`). A picture with numbers in it
is a typed number with a date on it. Re-shoot when a site changes, never edit the date by hand:

```bash
python3 -I scripts/shoot_sites.py /tmp/shots   # 1440x900 headless, then:
ffmpeg -i /tmp/shots/studio.png -q:v 3 assets/studio.jpg
ffmpeg -i /tmp/shots/<site>.png -vf scale=960:-1 -q:v 3 assets/sites/<site>.jpg
```

GIFs from other repos are linked by raw URL pinned to a tag or commit SHA, never `main`,
so a rename in that repo cannot break this page.

### `signature.svg` — Animated Hero Emblem

| Property | Value |
|----------|-------|
| **Type** | Inline SVG with CSS-only animations (no JavaScript) |
| **Dimensions** | 760 × 200 (`viewBox="0 0 760 200"`) — displayed at `width="600"` in README |
| **Color palette** | `#6C63FF` (primary), `#A78BFA` (secondary), `#818CF8` (tertiary) |
| **Theme support** | `prefers-color-scheme: light` swaps text fills — emblem colors stay constant |
| **Animations** | JD mark draws in, name rises, rule wipes, role fades; the resting state is the default, reduced motion disables all |
| **Referenced in** | `README.md` line 7 (`<img src="./signature.svg">`) — hero image, above the fold |

**Constraints:**
- Color values must stay in sync with Shields.io badge `color=6C63FF` used throughout README
- Subtitle text = brand identity titles (AI SOLUTIONS ENGINEER, CREATIVE TECHNOLOGIST, AUTONOMOUS AGENT BUILDER, MUSIC VIDEO DIRECTOR). These are **not** the same as Open To job targets — subtitles describe what James *is*, Open To lists what he's *seeking*. Do not "sync" these.
- Tagline stats ("47 REPOS", "24/7 AI ECOSYSTEM") must match badge and bio numbers (see FOR_DARE.md Metrics Sync Map)
- No external dependencies — the SVG is fully self-contained by design (replaced `readme-typing-svg`)

## See Also

- `FOR_DARE.md` — detailed project documentation, troubleshooting, badge services
