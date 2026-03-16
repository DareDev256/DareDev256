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
| Bump commit count | Search `1,257` in README.md — appears in 4 places (hero badge, Featured Projects, How We Work, Proof of Craft) |
| Add a new project | Add to the correct category table inside `<details>`, update repo count, update Featured if it's a flagship |
| Change job targets | Edit the "Open To" section header and evidence table |
| Test changes locally | `grip README.md` or push to a branch and preview at `github.com/DareDev256/DareDev256/blob/<branch>/README.md` |

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
32. **v0.7.9** (current) — Showcase updated to Passionate Learning Suite play page polish: visual loading spinner, engine startup refactor

**Lesson:** Profile READMEs are marketing documents. Structure them for the reader (recruiter, hiring manager), not for yourself.

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
The v0.7.0 restructure trimmed 20 sections to 12 visible + 4 collapsed. Every cut was intentional — deep content moved behind `<details>` toggles so the main scroll earns its space.

**Visible sections (in order):**
1. **Hero** — Custom animated emblem (`signature.svg`), bio, badge bar, CTA buttons
2. **Currently Building** — Status table (🟢/🟡) with live daily status from Passion Agent
3. **Workshop Showcase** — Latest build highlight, auto-updated by Passion Agent
4. **Featured Projects** — 2×3 HTML grid with stars, live links, and tech tags
5. **Open To** — Role targets with claim→evidence table
6. **Tech Stack** — `flat-square` badge grid
7. **Proof of Craft** — 5 verifiable claim→receipt pairs
8. **GitHub Stats** — Trophy shelf + profile summary cards (tokyonight theme)
9. **Closing CTA** — Quote, thesis, three action badges

**Collapsed sections (`<details>`):**
- **Domain Depth + Technical DNA** — expertise bar chart + architectural pattern table
- **How the Passion Ecosystem Works** — merged from 3 prior sections (How We Work, How Passion Ships, Glossary)
- **All 33 Projects** — 5 category tables
- **Hard Problems I've Solved** — 5 deep-dive war stories
- **What I'd Build Differently** — 4 honest retrospectives
- **Repo Setup & Dependencies** — fork instructions, external services, auto-update API docs

This 9+6 structure is not accidental — visible content converts in 5 seconds; collapsed content proves depth when engineers click through.

### Badge Style Consistency
All badges use `style=for-the-badge` for visual weight and consistency. Tech stack badges use `style=flat-square` for a more compact, scannable grid. This two-tier system creates visual hierarchy.

## Design Language

The README's visual identity is intentional — every color, badge style, and layout choice maps to a reason. This section exists so edits (human or agent) don't drift the visual system.

### Color Palette

| Color | Hex | Usage | Why |
|-------|-----|-------|-----|
| Indigo | `#6C63FF` | Primary brand — hero badges, CTA buttons, signature.svg emblem | Distinctive without being loud; reads well on both light and dark GitHub themes |
| Orchid | `#A855F7` | License badge, accent | Complements indigo without competing; signals "creative" |
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

1. Search the old number (e.g., `1,257`) — commit count appears in ~6 places
2. Update every instance — **do not leave stale numbers**, they undermine credibility
3. Update the corresponding badge in the hero section
4. Bump patch version, add CHANGELOG entry

### New Featured Project (Promote to Grid)

1. Replace the least-relevant cell in the Featured Projects `<table>`
2. Include: repo link, star badge (if public), bold one-liner, tech tags in backticks
3. Add matching entry to Currently Building table if actively developed
4. Ensure the project also exists in All Projects `<details>` section

### Seasonal Content Refresh

1. Update "What's Next" roadmap with current priorities
2. Verify "Open To" role targets match active job search
3. Check "The Arc" timeline — add milestones if new achievements landed
4. Review Proof of Craft — swap weakest claim→receipt for stronger evidence
5. Bump minor version (this is a content redesign)

## Metrics Sync Map

Every hardcoded number in the README must stay consistent across all its occurrences. This map shows exactly where each metric lives so updates never leave stale values behind.

### Commit Count (`1,257+`)

| Section | Context |
|---------|---------|
| Hero badges (line ~13) | `Total_Commits-1%2C257+` (URL-encoded) |
| Featured Projects | Passion Agent card: `1,257+ commits` |
| How the Passion Ecosystem (collapsed) | `1,257+ commits across ecosystem` |
| Proof of Craft | agent commit evidence |

**4 visible locations.** Source of truth: `git log --oneline | wc -l` across all managed repos.

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
| Currently Building | Passion Agent description |
| Featured Projects | Passion Agent card |
| How the Passion Ecosystem (collapsed) | architecture diagram |
| Domain Depth (collapsed) | Autonomous Systems evidence |

**4 locations.** Source of truth: Passion Agent codebase module count.

### LOC (`109K`)

| Section | Context |
|---------|---------|
| Currently Building | Passion Agent description |
| Featured Projects | Passion Agent card |
| How the Passion Ecosystem (collapsed) | architecture diagram |

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
| Currently Building | `ships across 47 repos` |
| Featured Projects | Passion Agent card |
| How the Passion Ecosystem (collapsed) | `47 Managed Repos` |
| Proof of Craft | `47 repos` |

**4 locations.** Source of truth: Passion Agent config repo list.

### fcpxml Stars (`20+`)

| Section | Context |
|---------|---------|
| Currently Building | `20+ stars` |
| Open To table | `20+ stars on first MCP server` |
| Proof of Craft | star evidence |

**3 locations.** Source of truth: `https://github.com/DareDev256/fcpxml-mcp-server` star count.

### Update Procedure

1. Search for the **exact current value** (e.g., `1,257`) — don't search just the number
2. Update every line listed above — **no partial updates**
3. For the commit badge (line 12), URL-encode commas as `%2C`
4. For The Arc section, maintain the narrative phrasing (e.g., "Then 1,257 more" not "1,257+ commits")
5. Bump patch version, add CHANGELOG entry

---

## Maintenance Checklist

When updating this README, verify:
- [ ] All project URLs still resolve (5 live deployments + GitHub links)
- [ ] Repo count is accurate (currently 33 public repos — includes awesome-mcp-servers fork)
- [ ] "Currently Building" section reflects actual current work
- [ ] Badge services are rendering (check for broken images on profile page)
- [ ] Stats cards are loading (github-profile-summary-cards.vercel.app)
- [ ] "Open To" section matches current job search status
- [ ] Collapsed "How the Passion Ecosystem Works" reflects current agent architecture
- [ ] CHANGELOG.md is updated with any changes (version bump for non-trivial changes)
- [ ] CHANGELOG versions are sequential with no gaps
- [ ] FOR_DARE.md version history matches CHANGELOG.md (Content Strategy Evolution section)

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

### Repo/commit counts are wrong
**Symptom:** Badge says "28 repos" but you have 30.
**Cause:** These are hardcoded in the README (not dynamic badges). They need manual updates.
**Fix:** Search the README for the stale number. Repo count appears in ~4 places, commit count in ~6. Update all instances, bump patch version, add CHANGELOG entry.

### Profile page looks different from raw README
**Symptom:** Layout or formatting differs between raw Markdown preview and the rendered profile.
**Cause:** GitHub's Markdown renderer strips certain HTML attributes (`style`, `class`, etc.) and has its own CSS. Inline `width` on `<td>` works, but `<div style="display:flex">` won't.
**Fix:** Only use GitHub-safe HTML: `align`, `width`, `height` attributes. Test on an actual branch push, not just a local Markdown previewer.
