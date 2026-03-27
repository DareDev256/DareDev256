# FOR_DARE.md — DareDev256 GitHub Profile README

## README Size Constraint (CRITICAL)

**The README.md MUST stay under 120 visible lines.** Total file can be ~300 lines with `<details>` blocks.

- **DO NOT add new visible sections.** If you need to add content, put it inside an existing `<details>` block.
- **DO NOT expand collapsed sections into visible content.**
- **DO NOT add ASCII art, timeline blocks, or multi-line code blocks** outside of `<details>`.
- **Auto-update zones** (`DAILY_STATUS_START/END`, `SHOWCASE_SECTION_START/END`) are fine — keep showcase to 1-2 lines max.
- **If adding a new project**: add it to the collapsed "All 33 Projects" details block, update the count. Do NOT add it to the visible Featured Projects table unless replacing an existing entry.
- **If updating metrics**: update in-place (badge numbers, table cells). Do NOT add new metric displays.

This constraint exists because a bloated profile README hurts more than it helps. Recruiters scan, they don't read. Every visible line must earn its place.

---

## Quick Reference

| Need to... | Do this |
|------------|---------|
| Update daily status | Passion Agent handles this automatically via `DAILY_STATUS_START/END` markers |
| Update showcase | Passion Agent writes between `SHOWCASE_SECTION_START/END` markers |
| Check badge health | Visit profile page, look for broken image icons. See [Troubleshooting](#troubleshooting) |
| Bump repo count | Search `33` in README.md — appears in 3 places (hero badge, Open To table, All Projects header) |
| Bump commit count | Search `1,257` in README.md — appears in 3 places (hero badge, Featured Projects, Proof of Craft) |
| Bump component count | Search `121` in README.md — appears in 5 places (see Metrics Sync Map: PACT Component Count) |
| Bump approval rate | Search `89.9` in README.md — appears in 4 places (see Metrics Sync Map: Approval Rate) |
| Add a new project | Add to the correct category table inside `<details>`, update repo count, update Featured if it's a flagship |
| Change job targets | Edit the "Open To" section header and evidence table |
| Test changes locally | `grip README.md` or push to a branch and preview at `github.com/DareDev256/DareDev256/blob/<branch>/README.md` |

### Pre-Push Quick Check (5-item fast path)

For Passion Agent's rapid iteration cycles — run this before every push. The full [Maintenance Checklist](#maintenance-checklist) covers edge cases; this covers the failures that actually recur.

1. **Version chain:** CHANGELOG heading = CLAUDE.md version field (e.g., both say `v0.8.23`)
2. **Metric consistency:** Any number you changed — search README for all occurrences (see [Metrics Sync Map](#metrics-sync-map))
3. **Content Strategy:** FOR_DARE.md Content Strategy Evolution ends with current version marked `(current)`
4. **Showcase URL:** If showcase zone was updated, verify the repo URL resolves (no spaces — [recurring bug](#showcase-url-has-broken-link-recurring))
5. **Line count:** `grep -c '' README.md` — must be under 400 total, visible sections under 120 lines

---

## What This Thing Actually Does

This repo powers the **GitHub profile README** — the first thing anyone sees when visiting [github.com/DareDev256](https://github.com/DareDev256). GitHub treats any repo named identically to your username as a special "profile" repo and renders its `README.md` directly on the profile page.

This is a **living document**, not code. It serves as a recruiter landing page, project portfolio, and personal brand statement. Every change here is immediately visible to anyone visiting the GitHub profile.

**Who cares:** Recruiters, potential collaborators, hiring managers, open-source community members. This is the digital storefront — it converts profile visits into LinkedIn connects, portfolio clicks, and job conversations.

## Architecture in Human Terms

There is no application architecture — this is a single Markdown file rendered by GitHub. The "system" is:

1. **README.md** — The entire product. GitHub-flavored Markdown with HTML for layout control.
2. **External badge services** — Dynamic images pulled from third-party APIs at render time.
3. **GitHub's rendering engine** — Converts Markdown + inline HTML into the profile page.

### Data Flow

```
README.md (static Markdown + HTML)
    ↓
GitHub Markdown Renderer
    ↓
Profile page at github.com/DareDev256
    ↕
External badge APIs (rendered as images):
  - komarev.com (profile view counter)
  - img.shields.io (all tech/project badges)
  - github-profile-summary-cards.vercel.app (stats cards)
  - github-profile-trophy.vercel.app (trophy shelf)
```

## Codebase Map

```
DareDev256/
├── README.md          # The entire product — GitHub profile page content
├── CHANGELOG.md       # Version history following Keep a Changelog format
├── CLAUDE.md          # Agent/contributor directives — size caps, auto-update zones
├── FOR_DARE.md        # This file — project documentation & troubleshooting
├── signature.svg      # Custom animated emblem — replaces generic typing SVG header
└── .git/              # Git version control
```

Five files. The simplicity is the point.

### File Cross-References & Editability

Every file references or constrains at least one other file. This map prevents edits that break cross-file contracts.

```
README.md ──img src──→ signature.svg (line 7, hero image)
    │
    ├── Uses color #6C63FF from signature.svg palette across 20+ Shields.io badges
    ├── Contains 2 machine-writable zones (DAILY_STATUS, SHOWCASE) written by Passion Agent
    └── Numbers (commits, repos, modules) must match Metrics Sync Map in FOR_DARE.md

CLAUDE.md ──defines rules for──→ README.md (size cap, structure, auto-update zones)
    │
    ├── References signature.svg constraints (color palette, subtitle text, tagline stats)
    └── Version field must match CHANGELOG.md latest heading

FOR_DARE.md ──documents──→ all files (architecture, playbooks, metrics, troubleshooting)
    │
    └── Metrics Sync Map tracks 13 hardcoded numbers across README.md locations

signature.svg ──standalone── (no outbound references — fully self-contained)
    │
    └── Color contract (#6C63FF, #A78BFA, #818CF8) consumed by README.md badges
```

| File | Editable By | Inbound References | Breakage Risk |
|------|:-----------:|-------------------|:-------------:|
| `README.md` | Human + Agent | Rendered by GitHub as profile page | **High** — visible to all visitors |
| `signature.svg` | Human only | `README.md` line 7 (`<img src>`) | **High** — hero visual, above the fold |
| `CLAUDE.md` | Human only | Agent reads before every task | Medium — wrong rules = wrong agent output |
| `FOR_DARE.md` | Human only | Referenced by CLAUDE.md "See Also" | Low — internal docs, not rendered |
| `CHANGELOG.md` | Human + Agent | Version must match CLAUDE.md | Low — not visitor-facing |

## Tech Stack & Why

| Technology | Purpose | Why This Choice |
|-----------|---------|-----------------|
| GitHub-Flavored Markdown | Content format | Only option for GitHub profile READMEs |
| Inline HTML (`<p>`, `<img>`, `<a>`) | Layout control | Markdown alone can't center content or control image sizing |
| Custom `signature.svg` | Animated hero emblem | Replaced third-party typing SVG — eliminates external dependency, branded identity |
| [Shields.io](https://shields.io) | Tech/project badges | Industry standard, huge icon library, `for-the-badge` style |
| [github-profile-summary-cards](https://github-profile-summary-cards.vercel.app) | Stats visualization | More reliable than github-readme-stats (which has frequent rate limiting) |
| [komarev.com](https://komarev.com/ghpvc/) | Profile view counter | Simple, free, no auth required |

### Rejected / Replaced Services

| Service | Why Replaced |
|---------|-------------|
| `readme-typing-svg` (demolab) | Replaced with custom `signature.svg` in v0.7.0 — eliminates external dependency, gives branded identity |
| `github-readme-stats` (anuraghazra) | Frequent downtime due to Vercel rate limits — cards often show as broken images |
| `github-readme-streak-stats` | Unreliable uptime, broken badges recurring issue |

### Signature SVG Architecture

The `signature.svg` (800×250, displayed at `width="600"`) is the hero visual — CSS-only animations, zero JavaScript, zero external dependencies. Understanding its layered animation system prevents accidental breakage during edits.

**Animation Sequence (8 systems, staggered over 5s):**

| Phase | Delay | System | What Happens |
|:-----:|------:|--------|-------------|
| 1 | 0.2s | `draw` | Infinity path draws in via `stroke-dashoffset` → 0 |
| 2 | 1.5–2.1s | `spin-cw/ccw` | 3 orbital ellipses fade in, rotate at different speeds (10s/13s/16s) |
| 3 | 2.0–2.6s | `pulse-r` | 3 electron dots pulse radius 5→8px on orbits |
| 4 | 2.5–3.2s | `fade` | Nucleus core + concentric rings materialize |
| 5 | 2.8–3.2s | `fade` + `ring-rotate` | Dharma wheel rings appear; dashed mid-ring rotates (20s loop) |
| 6 | 3.0–3.56s | `draw` | 8 spokes draw outward from center |
| 7 | 3.5–4.4s | `fade` | Arrow tips + segment arcs reveal on outer ring |
| 8 | 3.8–5.0s | `draw` + `fade` | Gradient divider draws, name fades in, subtitles begin cycling |

**Subtitle Cycle:** 4 titles rotate on a 12s loop (`t1`–`t4` keyframes): AI SOLUTIONS ENGINEER → CREATIVE TECHNOLOGIST → AUTONOMOUS AGENT BUILDER → MUSIC VIDEO DIRECTOR · 350+

**Color Contract:** `#6C63FF` (primary), `#A78BFA` (secondary), `#818CF8` (tertiary) — must match `color=6C63FF` on Shields.io badges throughout README.

**Theme Support:** `prefers-color-scheme: light` swaps name fill `#f0f0f0` → `#1a1a2e` and tagline fill `#555` → `#888`. Emblem colors are constant across themes.

**Edit Safety:** The emblem center is at `(130, 115)` — all spoke coordinates, ring radii, and orbit transforms reference this origin. Moving the center requires updating ~40 coordinate values.

## The War Stories

### Badge Reliability Wars (Feb 2026)
The original README used `github-readme-stats` for the stats cards. These broke repeatedly because the free Vercel deployment hits rate limits. Switched to `github-profile-summary-cards` which uses a different deployment strategy and has been stable since.

The streak stats badge also broke. Replaced with the `profile-details` card from summary-cards — one fewer external dependency, same information conveyed.

**Lesson:** Never depend on a single badge service for critical profile elements. Always have a fallback or use the more stable alternatives from the start.

### Content Strategy Evolution
The README went through several iterations (see CHANGELOG.md for full version history):
1. **v0.0.0** — Initial profile README, basic project list
2. **v0.1.0** — Added featured projects, star badges, profile view counter, "Currently Building" section
3. **v0.2.0** — Restructured for recruiter scanning: value proposition table, proof-based claims, "Open To" section, replaced unreliable badge services
4. **v0.3.0** — Typing animation header, `for-the-badge` style badges, FOR_DARE.md docs
5. **v0.4.0** — "How I Work" architecture diagram, sharpened Passion Agent narrative, closing CTA
6. **v0.4.1–v0.4.2** — CHANGELOG with proper semver, FOR_DARE.md docs, contribution model
7. **v0.5.0** — Visual redesign: centered hero, metrics ribbon, status table, HTML grid for featured projects, collapsible All Projects
8. **v0.6.0** — Project Goals, Contribution Guidelines, License/Repos/Deployments badges, quick-nav anchors
9. **v0.6.1** — Showcase highlights for TdotsSolutionsz design token system
10. **v0.6.2** — Metrics refresh: 145+ modules, 46K+ LOC, 36 repos, 1,257+ commits
11. **v0.6.3** — "The Arc" career timeline, "Proof of Craft" claim→receipt table, action-oriented CTAs
12. **v0.6.4** — FOR_DARE.md sync: updated layout map, version history, metrics, maintenance checklist
13. **v0.6.5** — Added Quick Reference card, Dynamic Content Zones docs, Troubleshooting guide, enhanced External Dependencies with health checks
14. **v0.6.6** — Vitest badge, security hardening evidence, updated memory-master-mvp description
15. **v0.6.7** — Fixed ASCII diagram alignment in "How We Work" section (title centering, 4 lines with wrong column width)
16. **v0.6.8** — Updated PACT Dashboard descriptions with signal-based auto-nav, keyboard shortcuts, iframe sandbox security; strengthened Proof of Craft with OWASP evidence
17. **v0.6.9** — Added Domain Depth visual expertise chart (replaced flat specializations line) and What's Next forward-looking roadmap section
18. **v0.6.10** — Added Design Language reference (color palette, badge hierarchy, layout rules, typography), Update Playbooks for common maintenance operations (new repo, metrics refresh, featured promotion, seasonal refresh)
19. **v0.6.11** — Added Metrics Sync Map to FOR_DARE.md — cross-reference index mapping 7 hardcoded metrics (commits, repos, modules, LOC, deployments, managed repos, fcpxml stars) to their exact README line numbers (37 total locations) with sources of truth and update procedure
20. **v0.6.12** — Added "Reading This? Start Here" audience-routing section (hiring managers, developers, AI enthusiasts, clients → targeted deep links). Fixed broken anchor link in quick-nav. Synced FOR_DARE.md Metrics Sync Map to match current README values (92 modules, 109K LOC, 47 managed repos, 29 public repos). Updated layout map to 19 sections
21. **v0.6.13** — Added "Engineering Principles" section between How We Work and Open To — 6 values (ship-first, accessibility, testing, security, open source, documentation) each with concrete "In Practice" evidence. Updated layout map to 20 sections
22. **v0.6.14** — Added hero tagline for cold-visitor context, velocity metrics ribbon (190 releases/21 days, 60 cycles/day, 89.9% approval, 1,237+ tests), strengthened closing thesis, updated What's Next with specific technical details and job targets
23. **v0.7.0** — Major trim: 760 → 301 lines. Cut 10 sections (Project Goals, Start Here, stats table, Recent Milestones, The Arc, Director's Eye, Engineering Principles, Behind This README, Contribution Guidelines, Security Policy). Collapsed deep content into 4 `<details>` blocks. Custom `signature.svg` replaces external typing SVG. Updated counts (121 components, 20+ stars, 53 tools)
24. **v0.7.1** — Portfolio-grade copy polish: tighter hero tagline, punchy bio, sharpened Featured Projects with unique value per card, stronger Proof of Craft receipts
25. **v0.7.2** — FOR_DARE.md major sync: layout map updated from stale 20-section structure to 9+4, added signature.svg and CLAUDE.md to codebase map, synced all Metrics Sync Map values
26. **v0.7.3** — Daily status and showcase zone refresh with PACT Dashboard security hardening + 43 new tests (695 total), ecosystem test total bumped to 1,350+
27. **v0.7.4** — Hero bio tightened ("Built and sold" KushdUp), Currently Building descriptions sharpened, Open To evidence rewritten with impact-first framing, footer quote refined
28. **v0.7.5** — Showcase updated to Passion Agent auto-select rules engine refactor, added helper extraction pattern to Hard Problems
29. **v0.7.6** — Synced test counts, refreshed showcase with unit test milestone (24 edge-case tests, 323 auto-select + 381 rotation tests)
30. **v0.7.7** — Added signature.svg type definition to CLAUDE.md (dimensions, color palette, animation contract, theme support, sync constraints)
31. **v0.7.8** — Added collapsed "Repo Setup & Dependencies" section: fork instructions, external service inventory, auto-update zone API documentation
32. **v0.7.9** — Showcase updated to Passionate Learning Suite play page polish: visual loading spinner, engine startup refactor
33. **v0.8.0** — Major FOR_DARE.md sync: fixed stale Content Strategy Evolution (stuck at v0.7.1), corrected collapsed section list (added Domain Depth + Repo Setup), updated Hard Problems count
34. **v0.8.1** — Restructured Repo Setup & Dependencies, sharpened Learning Suite description, linked Memory MCP
35. **v0.8.2** — Bumped ecosystem test totals (1,374+ → 1,400+), showcase updated to PACT envelope sanitizer (CWE-20/CWE-400/CWE-754), new Hard Problems entry
36. **v0.8.3** — Synced FOR_DARE.md with current state: fixed stale Content Strategy Evolution (stuck at v0.8.2), corrected troubleshooting example numbers, removed stale section references from playbooks, fixed Metrics Sync Map
37. **v0.8.4** — Fixed 3 stale references in FOR_DARE.md, synced version history
38. **v0.8.5** — Restructured Repo Setup & Dependencies: numbered replication steps, file inventory table, auto-update API reference with zone/marker/frequency breakdown. Synced FOR_DARE.md Content Strategy through v0.8.4
39. **v0.8.6** — Fixed Metrics Sync Map drift: corrected commit count locations (4→3, removed phantom ecosystem entry), fixed managed repos locations (swapped stale "Featured Projects" for actual "All Projects" row), added missing module count location (What I'd Build Differently, now 5), added exact context strings to all metric entries. Fixed Quick Reference and Metrics Refresh playbook with accurate counts
40. **v0.8.7** — Enhanced Repo Setup: editability matrix, impact ratings, auto-update format specs
41. **v0.8.8** — Fixed stale commit count reference in Troubleshooting (4→3, missed in v0.8.6 sync). Added Signature SVG Architecture section documenting all 8 animation systems, timing sequence, color palette contract, and theme-switch behavior
42. **v0.8.9** — Fixed stale cross-reference in Patterns Worth Stealing: All Projects category table count was 5 (never accurate), corrected to 4 (AI & Automation, Passionate Learning Suite, Interactive Web & Games, Client Websites)
43. **v0.8.10** — Fixed recurring broken showcase URL: Passion Agent auto-update re-introduced unencoded spaces in `tdotssolutionsz-portfolio` repo slug (same bug as v0.6.17)
44. **v0.8.11** — Added 2 missing projects to All Projects catalog (`passion-memory-server`, `DareDev256` self-reference), documented auto-update API field reference with formats/sources, added integration note for raw-file polling
45. **v0.8.12** — Synced Content Strategy Evolution through v0.8.11, added recurring URL encoding troubleshooting entry, added showcase URL validation to maintenance checklist
46. **v0.8.13** — Fixed stale Orchid hex in Design Language (`#A855F7` → `#A78BFA`), added self-documenting header to signature.svg (color contract, animation sequence, edit safety)
47. **v0.8.14** — Documented IntelDossier hero (animated threat indicators, tiered severity bars, source analysis) and intelligent video embed auto-selection across 4 README locations; updated showcase zone
48. **v0.8.15** — Updated PACT Dashboard descriptions to reflect Royalty Protocol hero (dynamic background video, scroll-triggered reveals, dark luxury aesthetic). Added cinematic hero orchestration to Hard Problems. Synced FOR_DARE.md Content Strategy through v0.8.14
49. **v0.8.16** — Fixed Hard Problems count drift (6→7), corrected CHANGELOG editability in Repo Setup (Human only→Human + Agent), added 2 missing metrics to Sync Map (test count 1,400+, release velocity 190)
50. **v0.8.17** — Added 4 missing metrics to Sync Map (PACT component count 121 in 5 locations, approval rate 89.9% in 4, PACT test count 695 in 4, fcpxml tool count 53 in 2), added Quick Reference entries for component count and approval rate, added Sync Map completeness check to Maintenance Checklist
51. **v0.8.18** — PACT Dashboard descriptions updated across 5 locations to reflect Purple Reign intro sequence (pulsating aura, metallic sheen reveal, dark luxury aesthetic). Showcase zone updated. BaseModal architecture and NavLink navigation component documented
52. **v0.8.19** — Fixed layout map section count (9→8 visible — showcase zone is part of Currently Building, not standalone). Added Version Milestones summary table for quick-scan of 52-entry Content Strategy. Synced Content Strategy through v0.8.18
53. **v0.8.20** — PACT Dashboard descriptions updated with auto-select engine. Proof of Craft quality claim sharpened. Auto-Update API docs expanded with raw endpoint and propagation timing
54. **v0.8.21** — Added MCP Protocol badge to Tech Stack, MCP & Integrations domain to expertise chart, MCP-native architecture pattern to Technical DNA. Promoted passion-memory-server to Featured Projects grid (replaced passion-site). Proof of Craft MCP claim expanded to cite both MCP servers. Synced Content Strategy through v0.8.20
55. **v0.8.22** — Fixed misleading SVG subtitle constraint in CLAUDE.md (subtitles ≠ Open To roles). Added Metric Verification Commands to FOR_DARE.md (one-liner per metric). Added Content Strategy drift troubleshooting entry. Sharpened README replication instructions for signature.svg. Updated Version Milestones
56. **v0.8.23** (current) — Added File Cross-References & Editability map to FOR_DARE.md (dependency graph + breakage risk matrix). Added Pre-Push Quick Check (5-item fast path for agent iteration). Improved README Repo Setup with architecture summary. Synced Content Strategy through v0.8.22

**Lesson:** Profile READMEs are marketing documents. Structure them for the reader (recruiter, hiring manager), not for yourself.

### Version Milestones (Quick Reference)

| Version | What Changed | Lines |
|---------|-------------|------:|
| **v0.1.0** | First real structure — featured projects, badges, view counter | ~150 |
| **v0.2.0** | Recruiter-optimized — value prop table, proof-based claims | ~200 |
| **v0.5.0** | Visual redesign — centered hero, metrics ribbon, HTML grid | ~350 |
| **v0.6.0** | Peak bloat — 20 sections, project goals, contribution guidelines | ~760 |
| **v0.7.0** | **Major trim** — 760→301 lines, 10 sections cut, custom `signature.svg` | ~301 |
| **v0.7.4** | Copy polish — tighter hero, impact-first Open To evidence | ~300 |
| **v0.8.0** | FOR_DARE.md sync era begins — Content Strategy tracking | ~300 |
| **v0.8.11** | All 33 projects cataloged, auto-update API documented | ~390 |
| **v0.8.18** | Purple Reign, BaseModal, NavLink — latest PACT Dashboard features | ~390 |
| **v0.8.21** | MCP-native era — protocol badge, expertise domain, architecture pattern, memory server promoted | ~393 |

The pattern: content grew until v0.6.0 (760 lines), got aggressively trimmed at v0.7.0 (301 lines), and has held steady at ~390 since. Growth now goes into collapsed `<details>` blocks, not visible surface area.

### Repo Count Accuracy
The README claims "33 public repos" — this includes the `awesome-mcp-servers` fork. If counting only original repos, it's 32. Keep this number updated as new repos are created.

## Dynamic Content Zones

Two sections of README.md are auto-updated by Passion Agent. They use HTML comment markers as boundaries — **never delete or rename these markers**.

### Daily Status Block

```
<!-- DAILY_STATUS_START -->
> *Updated by [Passion.EXE](...) — <date>*
> Today: **X tasks** across **Y repos** · ...
<!-- DAILY_STATUS_END -->
```

**Updated:** Every Passion Agent brain cycle that touches this repo (typically daily).
**What it shows:** Task count, repos touched, lines changed, success rate, latest task types.
**If it breaks:** The markers are intact but content is stale. Check Passion Agent logs for `daily-status` task failures.

### Showcase Block

```
<!-- SHOWCASE_SECTION_START -->
> *Last updated by [Passion Agent](...) — <date>*
**Tonight's build: [repo-name](...)**
...
<!-- SHOWCASE_SECTION_END -->
```

**Updated:** After notable builds, typically when Passion Agent completes a feature-level task on any repo.
**What it shows:** Latest shipped work with highlights and line count.
**If it breaks:** Check `passion-profile.mjs` in the Passion Agent codebase — that's the module responsible for showcase updates.

### Safe Editing Rule

You can freely edit anything **outside** these marker pairs. Content **inside** the markers will be overwritten by the next agent update. If you need to make a permanent change to the format of these sections, update the Passion Agent module that generates them.

---

## Patterns Worth Stealing

### Recruiter-Optimized Layout
The v0.7.0 restructure trimmed 20 sections dramatically, and subsequent refinements (v0.7.8 Repo Setup, v0.8.x Hard Problems additions) settled at 8 visible + 6 collapsed. Every cut was intentional — deep content moved behind `<details>` toggles so the main scroll earns its space.

**Visible sections (in order):**
1. **Hero** — Custom animated emblem (`signature.svg`), bio, badge bar, CTA buttons
2. **Currently Building** — Status table (🟢/🟡) + daily status zone + showcase zone (both auto-updated by Passion Agent)
3. **Featured Projects** — 2×3 HTML grid with stars, live links, and tech tags
4. **Open To** — Role targets with claim→evidence table
5. **Tech Stack** — `flat-square` badge grid
6. **Proof of Craft** — 5 verifiable claim→receipt pairs
7. **GitHub Stats** — Trophy shelf + profile summary cards (tokyonight theme)
8. **Closing CTA** — Quote, thesis, three action badges

**Collapsed sections (`<details>`):**
- **Domain Depth + Technical DNA** — expertise bar chart + architectural pattern table
- **How the Passion Ecosystem Works** — merged from 3 prior sections (How We Work, How Passion Ships, Glossary)
- **All 33 Projects** — 4 category tables
- **Hard Problems I've Solved** — 7 deep-dive war stories
- **What I'd Build Differently** — 4 honest retrospectives
- **Repo Setup & Dependencies** — fork instructions, external services, auto-update API docs

This 8+6 structure is not accidental — visible content converts in 5 seconds; collapsed content proves depth when engineers click through.

> **Note:** The showcase zone and daily status zone are embedded within "Currently Building" via HTML comment markers (`DAILY_STATUS_START/END`, `SHOWCASE_SECTION_START/END`), not standalone sections. Earlier versions of this map incorrectly counted the showcase as section 3.

### Badge Style Consistency
All badges use `style=for-the-badge` for visual weight and consistency. Tech stack badges use `style=flat-square` for a more compact, scannable grid. This two-tier system creates visual hierarchy.

## Design Language

The README's visual identity is intentional — every color, badge style, and layout choice maps to a reason. This section exists so edits (human or agent) don't drift the visual system.

### Color Palette

| Color | Hex | Usage | Why |
|-------|-----|-------|-----|
| Indigo | `#6C63FF` | Primary brand — hero badges, CTA buttons, signature.svg emblem | Distinctive without being loud; reads well on both light and dark GitHub themes |
| Orchid | `#A78BFA` | Subtitle cycling, orbit/electron accents, arrow tips, nucleus ring | Secondary brand color — used throughout signature.svg; see CLAUDE.md color contract |
| Emerald | `#10B981` | Live deployment badges, success states | Universal "live/active" signal; high contrast on dark backgrounds |
| Gold | `#FFD700` | Star badges, commit count | Maps to GitHub's own star color for instant recognition |
| Coral | `#FF6B6B` | AI ecosystem badge, passion.jamesdare.com CTA | Warm accent — stands out in the badge bar as the "human" element |
| Navy | `#0077B5` | LinkedIn badge | LinkedIn's exact brand color — don't change this |
| Black | `#000000` | X badge, Next.js/Vercel badges | Matches the services' own brand colors |

**Rule:** Never use generic Tailwind/Bootstrap palette colors. Every badge color either matches a brand (`#0077B5` for LinkedIn) or the profile's own palette (`#6C63FF` indigo).

### Badge Style Hierarchy

```
Hero section links:    style=for-the-badge  (large, action-oriented)
Metrics ribbon:        plain text with emoji  (scannable, no image load)
Tech stack grid:       style=flat-square     (compact, information-dense)
Project star counts:   style=flat-square     (subtle, secondary info)
```

This two-tier system creates visual weight where it matters (CTAs) and density where scanning matters (tech stack). Mixing styles within a tier breaks the hierarchy.

### Layout Rules

1. **Hero and closing CTA** use `<div align="center">` — everything else is left-aligned
2. **Featured Projects** use a `<table>` with `width="33%"` cells — not Markdown tables (which can't control column width)
3. **All Projects** live inside `<details>` to control scroll depth — never promote all 33 projects to top-level
4. **ASCII diagrams** use exactly 67 display columns — this is the widest that renders without horizontal scroll on mobile GitHub
5. **Sections flow** hook → proof → detail → CTA — never put detail before proof

### Typography

- **Signature SVG:** system-ui font stack (Segoe UI → system-ui → sans-serif), weight 800 for name, weight 500 for cycling subtitles, weight 300 for tagline. Colors: `#f0f0f0` name (swaps to `#1a1a2e` on light), `#A78BFA`/`#818CF8`/`#6C63FF` cycling subtitles, `#555` tagline (swaps to `#888` on light)
- **Code blocks:** Used for ASCII art and domain depth chart — never for inline code snippets (use backtick spans instead)
- **Emphasis pattern:** Bold for project names and metrics, italic for dates and attributions, never underline

## Level-Up Takeaways

- **GitHub profile READMEs are marketing, not documentation.** Optimize for the reader's goals (hiring, collaborating), not your own completeness.
- **External service reliability matters.** Badge services go down. Use stable providers, have fallbacks, and don't depend on free-tier Vercel deployments for critical visibility.
- **Information hierarchy is everything.** The most important content (who you are, what you're building, how to reach you) must be above the fold.
- **Keep it current.** A stale profile README is worse than none — it signals inactivity. The "Currently Building" section and live demo links prove ongoing work.

## How Changes Get Made (Contribution Model)

This repo is maintained by two contributors:

1. **James (DareDev256)** — Direct commits to `main` for manual updates, content rewrites, and PR reviews.
2. **Passion Agent** — Autonomous AI agent running 24/7 on a Mac Mini. Creates feature branches, makes improvements, and opens PRs for human review.

### Passion Agent Branch Convention

```
passion/<task-type>-<descriptor>-<id>
```

Examples:
- `passion/docs-diversity-picked-docs-mlfbszxo`
- `passion/improve-auto-mlb4265p`
- `passion/refactor-cooldown-forced-focus-on-mld34kxo`

### Valid Task Types for This Repo

Only `readme` and `docs` tasks are valid here — this is a documentation-only repo with no application code. The agent should never attempt code-type tasks (test, refactor, feature) on this repo.

### PR Review Flow

```
Passion Agent creates branch → pushes changes → opens PR
    ↓
James reviews on GitHub (or via Discord notification)
    ↓
Merge or reject → Passion Agent learns from the decision
```

The agent's learning engine (`passion-learn.mjs`) tracks which PRs get merged vs rejected and adjusts future behavior accordingly.

## Update Playbooks

Step-by-step procedures for the most common maintenance operations. Follow these exactly to avoid inconsistencies.

### New Repo Added

1. Add entry to the correct category table inside `<details>` in All Projects
2. Search `33` (or current count) → update in 3 places: hero badge, Open To table, All Projects header
3. If it's a flagship: add to Featured Projects `<table>` grid (max 6 cells — 2 rows of 3)
4. If it has live deployment: add `[![Live](badge)](url)` inline
5. Bump patch version, add CHANGELOG entry

### Metrics Refresh (Commits, Stars, Modules)

1. Search the old number (e.g., `1,257`) — commit count appears in 3 places (see Metrics Sync Map)
2. Update every instance — **do not leave stale numbers**, they undermine credibility
3. Update the corresponding badge in the hero section
4. Bump patch version, add CHANGELOG entry

### New Featured Project (Promote to Grid)

1. Replace the least-relevant cell in the Featured Projects `<table>`
2. Include: repo link, star badge (if public), bold one-liner, tech tags in backticks
3. Add matching entry to Currently Building table if actively developed
4. Ensure the project also exists in All Projects `<details>` section

### Seasonal Content Refresh

1. Verify "Open To" role targets match active job search
2. Review "Currently Building" table — swap out completed/stale projects
3. Review Proof of Craft — swap weakest claim→receipt for stronger evidence
4. Check collapsed "Hard Problems" and "What I'd Build Differently" — add new entries if applicable
5. Bump minor version (this is a content redesign)

## Metrics Sync Map

Every hardcoded number in the README must stay consistent across all its occurrences. This map shows exactly where each metric lives so updates never leave stale values behind.

### Commit Count (`1,257+`)

| Section | Context |
|---------|---------|
| Hero badges (line ~13) | `Total_Commits-1%2C257+-` (URL-encoded comma) |
| Featured Projects | Passion Agent card: `89.9% approval across 1,257+ commits` |
| Proof of Craft | `1,257+ commits across 47 repos` |

**3 locations.** Source of truth: `git log --oneline | wc -l` across all managed repos.

### Public Repo Count (`33`)

| Section | Context |
|---------|---------|
| Hero badges (line ~10) | `Public_Repos-33` |
| Open To table | shipping velocity evidence |
| All Projects header (collapsed) | `All 33 Projects` |

**3 locations.** Source of truth: `https://github.com/DareDev256?tab=repositories`.

### Module Count (`92`)

| Section | Context |
|---------|---------|
| Currently Building | `92 modules, 109K LOC` |
| Featured Projects | Passion Agent card: `92 modules, 109K LOC` |
| How the Passion Ecosystem (collapsed) | architecture diagram: `92 modules, 109K LOC` |
| Domain Depth (collapsed) | Autonomous Systems: `24/7 agent ops, 92 modules` |
| What I'd Build Differently (collapsed) | `Single config.json at 92 modules` |

**5 locations.** Source of truth: Passion Agent codebase module count.

### LOC (`109K`)

| Section | Context |
|---------|---------|
| Currently Building | `92 modules, 109K LOC` |
| Featured Projects | Passion Agent card: `92 modules, 109K LOC` |
| How the Passion Ecosystem (collapsed) | diagram: `92 modules, 109K LOC` |

**3 locations.** Source of truth: `cloc` or `tokei` on the Passion Agent repo.

### Live Deployments (`20+`)

| Section | Context |
|---------|---------|
| Hero badges (line ~12) | `Live_Deployments-20+` |
| Open To table | shipping velocity evidence |

**2 locations.** Source of truth: count of Vercel deployments + GitHub Pages sites.

### Managed Repos (`47`)

| Section | Context |
|---------|---------|
| Currently Building | `opens PRs across 47 repos` |
| Proof of Craft | `1,257+ commits across 47 repos` |
| How the Passion Ecosystem (collapsed) | `47 Managed Repos` diagram line |
| All 33 Projects (collapsed) | Passion Agent row: `24/7 brain cycles, 47 repos` |

**4 locations.** Source of truth: Passion Agent config repo list.

### fcpxml Stars (`20+`)

| Section | Context |
|---------|---------|
| Currently Building | `20+ stars` |
| Open To table | `20+ stars on first MCP server` |
| Proof of Craft | star evidence |

**3 locations.** Source of truth: `https://github.com/DareDev256/fcpxml-mcp-server` star count.

### Ecosystem Test Count (`1,400+`)

| Section | Context |
|---------|---------|
| Open To table | `1,400+ tests across ecosystem` |
| Proof of Craft | `1,400+ tests across the ecosystem. 695 in one repo alone` |

**2 locations.** Source of truth: aggregate test count across all repos (`npm test` / `vitest` / `pytest` totals).

### Release Velocity (`190`)

| Section | Context |
|---------|---------|
| Open To table | `190 releases in 21 days` |
| Proof of Craft | `190 releases in 21 days` |

**2 locations.** Source of truth: `gh release list` across all repos within the measured period.

### PACT Component Count (`121`)

| Section | Context |
|---------|---------|
| Currently Building | `121 components, 695 tests, OWASP-hardened` |
| Featured Projects | PACT Dashboard card: `121 components. 695 tests` |
| How the Passion Ecosystem (collapsed) | diagram: `Royalty Protocol hero, 121 components` |
| All 33 Projects (collapsed) | PACT Dashboard row: `121 components, 695 tests` |
| What I'd Build Differently (collapsed) | `121 components, not enough composition` |

**5 locations.** Source of truth: PACT Dashboard component directory count.

### Approval Rate (`89.9%`)

| Section | Context |
|---------|---------|
| Currently Building | Passion Agent: `89.9% approval rate` |
| Featured Projects | Passion Agent card: `89.9% approval across 1,257+ commits` |
| Domain Depth (collapsed) | `89.9% approval rate as a live metric` |
| How the Passion Ecosystem (collapsed) | diagram: `89.9% autonomous approval rate` |

**4 locations.** Source of truth: Passion Agent merged-vs-rejected PR ratio.

### PACT Test Count (`695`)

| Section | Context |
|---------|---------|
| Currently Building | `121 components, 695 tests` |
| Featured Projects | PACT Dashboard card: `695 tests, OWASP-hardened` |
| Proof of Craft | `695 in one repo alone` |
| All 33 Projects (collapsed) | PACT Dashboard row: `695 tests, OWASP-hardened` |

**4 locations.** Source of truth: PACT Dashboard test suite count (`vitest --reporter=verbose | tail -1`).

### fcpxml Tool Count (`53`)

| Section | Context |
|---------|---------|
| Currently Building | `53 tools, natural language timeline editing` |
| Featured Projects | fcpxml card: `53 tools — timeline analysis, health checks` |

**2 locations.** Source of truth: `fcpxml-mcp-server` tool registry count.

### Update Procedure

1. Search for the **exact current value** (e.g., `1,257`) — don't search just the number
2. Update every line listed above — **no partial updates**
3. For the commit badge (line ~13), URL-encode commas as `%2C`
4. Keep phrasing consistent with surrounding context (e.g., "1,257+ commits across 47 repos")
5. Bump patch version, add CHANGELOG entry

### Metric Verification Commands

One-liner for each source of truth. Run these before updating numbers in the README.

| Metric | Command |
|--------|---------|
| Commit count | `cd ~/dev/passion-agent && git log --oneline --all \| wc -l` (aggregate across managed repos) |
| Public repo count | `curl -s "https://api.github.com/users/DareDev256" \| jq .public_repos` |
| Module count | `ls -d ~/dev/passion-agent/modules/*/ \| wc -l` |
| LOC | `tokei ~/dev/passion-agent --sort code` (or `cloc`) |
| Live deployments | `grep -c "vercel.app" ~/dev/passion-agent/config.json` (approximate) |
| Managed repos | `jq '.repos \| length' ~/dev/passion-agent/config.json` |
| fcpxml stars | `curl -s "https://api.github.com/repos/DareDev256/fcpxml-mcp-server" \| jq .stargazers_count` |
| Ecosystem tests | Aggregate: `npm test` / `vitest` / `pytest` across all repos |
| PACT components | `find ~/dev/passion-dashboard/src/components -name "*.tsx" \| wc -l` |
| PACT tests | `cd ~/dev/passion-dashboard && npx vitest --reporter=verbose 2>&1 \| tail -1` |
| Approval rate | Passion Agent's `passion-learn.mjs` merged÷total ratio |
| fcpxml tools | `grep -c "def.*tool" ~/dev/fcpxml-mcp-server/src/*.py` (approximate) |

> **Note:** GitHub API has a 60 req/hr unauthenticated rate limit. For bulk checks, use `gh api` (authenticated) instead of `curl`.

---

## Maintenance Checklist

When updating this README, verify:
- [ ] All project URLs still resolve (20+ live deployments + GitHub links)
- [ ] Repo count is accurate (currently 33 public repos — includes awesome-mcp-servers fork)
- [ ] "Currently Building" section reflects actual current work
- [ ] Badge services are rendering (check for broken images on profile page)
- [ ] Stats cards are loading (github-profile-summary-cards.vercel.app)
- [ ] "Open To" section matches current job search status
- [ ] Collapsed "How the Passion Ecosystem Works" reflects current agent architecture
- [ ] CHANGELOG.md is updated with any changes (version bump for non-trivial changes)
- [ ] Showcase section URL resolves (no spaces in repo slug — recurring bug, see Troubleshooting)
- [ ] CHANGELOG versions are sequential with no gaps
- [ ] All 13 Sync Map metrics are consistent across their documented locations
- [ ] FOR_DARE.md Content Strategy Evolution synced through current version (check "(current)" marker)

## External Dependencies (Badge Services)

All rendering depends on external services. If any break, the profile degrades visually:

| Service | URL | Health Check | Fallback |
|---------|-----|-------------|----------|
| Shields.io | img.shields.io | [Test](https://img.shields.io/badge/test-passing-green) | Plain text in parentheses |
| Profile Summary Cards | github-profile-summary-cards.vercel.app | [Test](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=DareDev256&theme=tokyonight) | Remove stats section entirely |
| Profile Trophy | github-profile-trophy.vercel.app | [Test](https://github-profile-trophy.vercel.app/?username=DareDev256&theme=tokyonight&no-frame=true&column=1) | Remove trophy shelf |
| Komarev Views | komarev.com | [Test](https://komarev.com/ghpvc/?username=DareDev256) | Remove view counter badge |

---

## Troubleshooting

### Broken badge images on profile
**Symptom:** One or more badges render as broken image icons or alt text.
**Cause:** External badge service is down or rate-limited.
**Fix:** Click the health check links above. If the service is down, either wait (usually recovers in hours) or temporarily replace with static text. Shields.io is the most critical — if it goes down, 20+ badges break simultaneously.

### Stats cards not loading
**Symptom:** GitHub Stats section shows broken images.
**Cause:** `github-profile-summary-cards.vercel.app` hit Vercel's free-tier rate limit.
**Fix:** These are the *replacement* for the even-more-unreliable `github-readme-stats`. If they break persistently, consider self-hosting the summary cards app (it's [open source](https://github.com/vn7n24fzkq/github-profile-summary-cards)).

### Daily status shows stale date
**Symptom:** The "Updated by Passion.EXE" timestamp is days old.
**Cause:** Passion Agent's brain cycle hasn't run the daily-status task, or it failed.
**Fix:** Check Passion Agent logs. The daily status update is a low-priority task — it only runs when the agent has spare cycles. You can trigger it manually by running the profile update module.

### Showcase URL has broken link (RECURRING)
**Symptom:** Showcase section links to a GitHub URL with `%20` or literal spaces — returns 404.
**Cause:** Passion Agent's `passion-profile.mjs` generates the showcase repo name from the task description, which may contain spaces. GitHub URLs require hyphenated slugs, not spaces.
**History:** First hit in v0.6.17, recurred in v0.8.10. Same root cause both times — the agent's profile writer doesn't slugify repo names.
**Fix:** Verify the URL resolves before committing. The repo slug must be lowercase-hyphenated (e.g., `tdotssolutionsz-portfolio`, not `TdotsSolutionsz Music Video Portfolio`). Long-term fix: add URL validation to `passion-profile.mjs` before writing the showcase zone.

### Repo/commit counts are wrong
**Symptom:** Badge says "33 repos" but you have 35.
**Cause:** These are hardcoded in the README (not dynamic badges). They need manual updates.
**Fix:** Search the README for the stale number. See the Metrics Sync Map above for exact locations. Repo count appears in 3 places, commit count in 3. Update all instances, bump patch version, add CHANGELOG entry.

### Content Strategy Evolution gets stuck (RECURRING)
**Symptom:** FOR_DARE.md's Content Strategy list has "(current)" on an old version, missing recent entries.
**Cause:** When Passion Agent updates FOR_DARE.md, it often syncs only some sections and misses the Content Strategy. This has recurred at v0.7.1 (fixed v0.8.0), v0.8.2 (fixed v0.8.3), and v0.8.14 (fixed v0.8.15).
**Fix:** After any version bump, verify the Content Strategy list ends with the new version marked as "(current)". Add missing intermediate entries from CHANGELOG.md. The Maintenance Checklist already tracks this — look for "Content Strategy Evolution synced through current version".

### Profile page looks different from raw README
**Symptom:** Layout or formatting differs between raw Markdown preview and the rendered profile.
**Cause:** GitHub's Markdown renderer strips certain HTML attributes (`style`, `class`, etc.) and has its own CSS. Inline `width` on `<td>` works, but `<div style="display:flex">` won't.
**Fix:** Only use GitHub-safe HTML: `align`, `width`, `height` attributes. Test on an actual branch push, not just a local Markdown previewer.
