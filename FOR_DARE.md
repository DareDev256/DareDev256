# FOR_DARE.md — DareDev256 GitHub Profile README

## Quick Reference

| Need to... | Do this |
|------------|---------|
| Update daily status | Passion Agent handles this automatically via `DAILY_STATUS_START/END` markers |
| Update showcase | Passion Agent writes between `SHOWCASE_SECTION_START/END` markers |
| Check badge health | Visit profile page, look for broken image icons. See [Troubleshooting](#troubleshooting) |
| Bump repo count | Search `29` in README.md — appears in 4+ places (badges, metrics ribbon, All Projects header, Open To table, The Arc) |
| Bump commit count | Search `1,257` in README.md — appears in 6 places (badges, metrics ribbon, Currently Building, How We Work, The Arc, Proof of Craft) |
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
  - readme-typing-svg.demolab.com (animated typing header)
  - komarev.com (profile view counter)
  - img.shields.io (all tech/project badges)
  - github-profile-summary-cards.vercel.app (stats cards)
```

## Codebase Map

```
DareDev256/
├── README.md          # The entire product — GitHub profile page content
├── CHANGELOG.md       # Version history following Keep a Changelog format
├── FOR_DARE.md        # This file — project documentation
└── .git/              # Git version control
```

Three files. The simplicity is the point.

## Tech Stack & Why

| Technology | Purpose | Why This Choice |
|-----------|---------|-----------------|
| GitHub-Flavored Markdown | Content format | Only option for GitHub profile READMEs |
| Inline HTML (`<p>`, `<img>`, `<a>`) | Layout control | Markdown alone can't center content or control image sizing |
| [readme-typing-svg](https://readme-typing-svg.demolab.com) | Animated header | Eye-catching, configurable, no JS required |
| [Shields.io](https://shields.io) | Tech/project badges | Industry standard, huge icon library, `for-the-badge` style |
| [github-profile-summary-cards](https://github-profile-summary-cards.vercel.app) | Stats visualization | More reliable than github-readme-stats (which has frequent rate limiting) |
| [komarev.com](https://komarev.com/ghpvc/) | Profile view counter | Simple, free, no auth required |

### Rejected / Replaced Services

| Service | Why Replaced |
|---------|-------------|
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
21. **v0.6.13** (current) — Added "Engineering Principles" section between How We Work and Open To — 6 values (ship-first, accessibility, testing, security, open source, documentation) each with concrete "In Practice" evidence. Updated layout map to 20 sections

**Lesson:** Profile READMEs are marketing documents. Structure them for the reader (recruiter, hiring manager), not for yourself.

### Repo Count Accuracy
The README claims "29 public repos" — this includes the `awesome-mcp-servers` fork. If counting only original repos, it's 28. Keep this number updated as new repos are created.

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
The README follows a deliberate information hierarchy:
1. **Hook** — Typing animation with role titles
2. **One-liner** — Who you are, what you've done, compressed into one paragraph
3. **Metrics ribbon** — Gold record, repos, stars, deployments, commits, AI ecosystem at a glance
4. **Project Goals** — What drives every repo (shipped AI, build in public, creative-technical bridge, autonomous collaboration)
5. **Reading This? Start Here** — Audience-targeted navigation: hiring managers → proof, developers → architecture, AI enthusiasts → ecosystem, clients → portfolio
6. **Currently Building** — Status table (🟢/🟡) with live daily status from Passion Agent
7. **Workshop Showcase** — Latest build highlight, auto-updated by Passion Agent
8. **Featured Projects** — 2×3 HTML grid with stars, live links, and tech tags
9. **How We Work** — ASCII architecture diagram showing the Passion ecosystem
10. **Engineering Principles** — 6 values (ship-first, accessibility, testing, security, open source, documentation) with "In Practice" evidence
11. **Open To** — Explicit role targeting with claim→evidence table
12. **All Projects** — Categorized tables inside `<details>` toggle (29 projects across 5 categories)
13. **Tech Stack** — Two-tier badges: `for-the-badge` for links, `flat-square` for tech grid
14. **Domain Depth** — Unicode bar chart showing expertise levels across 7 domains with evidence callout
15. **GitHub Stats** — Profile summary cards (tokyonight theme)
16. **The Arc** — Visual career timeline (2008→2026) using tree characters
17. **Proof of Craft** — 5 verifiable claim→receipt pairs with direct links to evidence
18. **What's Next** — Forward-looking roadmap (current, next, goal) in tree-character format
19. **Contribution Guidelines** — Fork workflow, conventional commits, PR etiquette
20. **Closing CTA** — Quote, thesis statement, three action badges

This 20-section structure is not accidental — it's designed to capture attention in the first 5 seconds and give recruiters a reason to click through.

### Badge Style Consistency
All badges use `style=for-the-badge` for visual weight and consistency. Tech stack badges use `style=flat-square` for a more compact, scannable grid. This two-tier system creates visual hierarchy.

## Design Language

The README's visual identity is intentional — every color, badge style, and layout choice maps to a reason. This section exists so edits (human or agent) don't drift the visual system.

### Color Palette

| Color | Hex | Usage | Why |
|-------|-----|-------|-----|
| Indigo | `#6C63FF` | Primary brand — hero badges, CTA buttons, typing SVG | Distinctive without being loud; reads well on both light and dark GitHub themes |
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
3. **All Projects** live inside `<details>` to control scroll depth — never promote all 28 projects to top-level
4. **ASCII diagrams** use exactly 67 display columns — this is the widest that renders without horizontal scroll on mobile GitHub
5. **Sections flow** hook → proof → detail → CTA — never put detail before proof

### Typography

- **Typing SVG:** Fira Code weight 600, size 22, color `#6C63FF`, 1000ms pause
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
2. Search `28` (or current count) → update in 4 places: badge, metrics ribbon, All Projects header, Open To table
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

| Line | Section | Context |
|------|---------|---------|
| 12 | Hero badges | `Total_Commits-1%2C257+` (URL-encoded) |
| 26 | Metrics ribbon | `1,257+ Commits` |
| 47 | Currently Building | Passion Agent description |
| 104 | Featured Projects | Passion Agent card |
| 176 | How We Work diagram | `1,257+ commits across ecosystem` |
| 205 | Open To table | shipping velocity evidence |
| 219 | All Projects | Passion Agent row |
| 348 | The Arc | `Then 1,257 more` |
| 366 | Proof of Craft | agent commit evidence |

**9 locations.** Source of truth: `git log --oneline | wc -l` across all 36 managed repos.

### Public Repo Count (`29`)

| Line | Section | Context |
|------|---------|---------|
| 9 | Hero badges | `Public_Repos-29` |
| 26 | Metrics ribbon | `29 Public Repos` |
| ~77 | Quick links | `All 29 Projects` anchor text |
| ~215 | Open To table | shipping velocity evidence |
| ~222 | All Projects header | `All 29 Projects` |
| ~363 | The Arc | `29 repos` |

**6 locations.** Source of truth: `https://github.com/DareDev256?tab=repositories` (includes awesome-mcp-servers fork).

### Module Count (`92`)

| Line | Section | Context |
|------|---------|---------|
| ~57 | Currently Building | Passion Agent description (`92 modules`) |
| ~114 | Featured Projects | Passion Agent card (`92 modules`) |
| ~175 | How We Work diagram | `92 modules, 109K LOC` |
| ~229 | All Projects | Passion Agent row |
| ~322 | Domain Depth | Autonomous Systems evidence (`92 modules`) |
| ~363 | The Arc | `92 modules` |

**6 locations.** Source of truth: Passion Agent codebase module count.

### LOC (`109K`)

| Line | Section | Context |
|------|---------|---------|
| ~57 | Currently Building | Passion Agent description (`109K LOC`) |
| ~114 | Featured Projects | Passion Agent card (`109K LOC`) |
| ~175 | How We Work diagram | `92 modules, 109K LOC` |

**3 locations.** Source of truth: `cloc` or `tokei` on the Passion Agent repo.

### Live Deployments (`16+`)

| Line | Section | Context |
|------|---------|---------|
| 11 | Hero badges | `Live_Deployments-16+` |
| 26 | Metrics ribbon | `16+ Live Deployments` |
| 205 | Open To table | shipping velocity evidence |
| 350 | The Arc | `16+ live deployments` |

**4 locations.** Source of truth: count of Vercel deployments + GitHub Pages sites.

### Managed Repos (`47`)

| Line | Section | Context |
|------|---------|---------|
| ~57 | Currently Building | `Orchestrates 47 repos` |
| ~114 | Featured Projects | `47 managed repos` |
| ~186 | How We Work diagram | `47 Managed Repos` |
| ~229 | All Projects | `47 repos` |
| ~376 | Proof of Craft | `47 repos` |

**5 locations.** Source of truth: Passion Agent config repo list.

### fcpxml Stars (`16`)

| Line | Section | Context |
|------|---------|---------|
| 49 | Currently Building | `16 stars` |
| 207 | Open To table | `16 stars on first MCP server` |
| 349 | The Arc | `16 stars` |
| 364 | Proof of Craft | `16 stars, 2 forks` |

**4 locations.** Source of truth: `https://github.com/DareDev256/fcpxml-mcp-server` star count.

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
- [ ] Repo count is accurate (currently 29 public repos — includes awesome-mcp-servers fork)
- [ ] "Currently Building" section reflects actual current work
- [ ] Badge services are rendering (check for broken images on profile page)
- [ ] Stats cards are loading (github-profile-summary-cards.vercel.app)
- [ ] "Open To" section matches current job search status
- [ ] "How I Work" diagram reflects current Passion Agent module architecture
- [ ] CHANGELOG.md is updated with any changes (version bump for non-trivial changes)
- [ ] CHANGELOG versions are sequential with no gaps
- [ ] FOR_DARE.md version history matches CHANGELOG.md (Content Strategy Evolution section)

## External Dependencies (Badge Services)

All rendering depends on external services. If any break, the profile degrades visually:

| Service | URL | Health Check | Fallback |
|---------|-----|-------------|----------|
| Typing SVG | readme-typing-svg.demolab.com | [Test](https://readme-typing-svg.demolab.com?lines=test) | Static `# James Dare` header |
| Shields.io | img.shields.io | [Test](https://img.shields.io/badge/test-passing-green) | Plain text in parentheses |
| Profile Summary Cards | github-profile-summary-cards.vercel.app | [Test](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=DareDev256&theme=tokyonight) | Remove stats section entirely |
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
