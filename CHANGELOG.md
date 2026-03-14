# Changelog

All notable changes to the DareDev256 GitHub profile README are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/): major = full redesign, minor = new sections, patch = fixes/updates.

## [Unreleased]

## [0.7.6] - 2026-03-13

### Changed
- **Showcase zone** — updated to auto-select unit test milestone: 24 targeted tests covering null-seed folding, deep-freeze contracts, NaN/clamp boundaries (323 auto-select + 381 rotation tests green)
- **Ecosystem test total** — bumped 1,350+ → 1,374+ across Open To and Proof of Craft sections
- **Hard Problems** — helper extraction entry updated with unit test coverage milestone (24 edge-case tests)
- **What I'd Build Differently** — fixed fcpxml-mcp-server test count drift: 571 → 618 (matching actual state)

## [0.7.5] - 2026-03-13

### Changed
- **Showcase zone** — updated to Passion Agent auto-select rules engine refactor (computeEntryTiming, freezeActivityMap, maxSeverity)
- **Hard Problems I've Solved** — added helper extraction pattern: centralized duplicated timing guards, freeze loops, and ternary accumulation into three focused functions (-17 net lines, 381 tests passing)

## [0.7.4] - 2026-03-13

### Changed
- **Hero bio** — tighter transition narrative: "Built and sold" KushdUp, "architect AI systems that run 24/7" over passive phrasing
- **Currently Building** — Passion Agent row leads with approval rate, fcpxml sharpened to "timeline editing", Learning Suite emphasizes "each deployed, each playable"
- **Open To** — "Solutions Engineer" → "Solutions Architect", evidence column rewritten with stronger proof framing ("in production, not slides", "solo")
- **Proof of Craft** — receipts tightened: ecosystem test total leads ("1,350+ tests across the ecosystem"), "No demo — just merged PRs"
- **Featured Projects** — PACT and Passion Agent descriptions tightened for scannability
- **Footer quote** — "Same eye that framed a music video now frames a system architecture" replaces generic directing metaphor
- **Ecosystem details** — "merged PR" replaces "PR creation" to signal completion, not just initiation

## [0.7.3] - 2026-03-13

### Changed
- **Daily status zone** — refreshed to Mar 13 with current task stats (4 tasks, 3 repos, 100% success)
- **Showcase zone** — updated to PACT Dashboard four-layer security hardening + 43 new tests (695 total, 14 suites)
- **Test counts updated** — PACT Dashboard 571→695 across Proof of Craft, Open To, Featured Projects, Currently Building, and All Projects sections
- **PACT descriptions tightened** — replaced "keyboard shortcuts, voice control" with "695 tests, OWASP-hardened" to lead with quality signals
- **Ecosystem test total** — bumped from 1,237+ to 1,350+ reflecting PACT and fcpxml-mcp-server growth

## [0.7.2] - 2026-03-11

### Changed
- **FOR_DARE.md major sync** — documentation drifted during v0.7.x restructure, now reflects actual state
- Updated layout map from stale 20-section structure to current 9 visible + 4 collapsed architecture
- Added `signature.svg` and `CLAUDE.md` to codebase map (were missing since v0.7.0)
- Synced all Metrics Sync Map values: repos 29→33, stars 16→20+, deployments 16+→20+, removed stale line-number refs
- Updated version history through v0.7.1 (was stuck at v0.6.14)
- Replaced typing SVG references with custom `signature.svg` in tech stack, data flow, and external deps tables
- Added trophy shelf to external dependencies with health check link
- Updated maintenance checklist and playbook counts to match current repo state

## [0.7.1] - 2026-03-11

### Changed
- Hero tagline tightened — "ship code while I sleep" over generic "24/7" phrasing
- Bio restructured from single run-on sentence to punchy short statements
- Currently Building descriptions sharpened — each row now highlights what's unique, not repeated stats
- Featured Projects copy rewritten — Passion Agent shows approval rate, PACT shows real-time monitoring, pulsemap shows animated arcs
- Open To evidence column strengthened with impact-first framing ("shipped, not demoed")
- Proof of Craft receipts polished for scannability — tighter phrasing, stronger verbs
- Closing quote refined — "infinite scale" replaces "but now it scales"

## [0.7.0] - 2026-03-11

### Changed
- **Major trim: 760 → 301 lines** (117 visible, 118 in collapsed details)
- Cut 10 sections: Project Goals, Start Here nav, stats table, Recent Milestones, The Arc, Director's Eye, Engineering Principles, Behind This README, Contribution Guidelines, Security Policy
- Merged "How We Work" + "How Passion Ships" + Glossary into single collapsed "How the Passion Ecosystem Works"
- Merged "Technical DNA" + "Domain Depth" into collapsed Tech Stack details block
- Condensed showcase section to single line instead of multi-line block
- Updated UIVPG link to clean Vercel URL (ultimate-image-prompt-generator.vercel.app)
- Updated component counts (101 → 121), star counts (19 → 20+), tool count (34 → 53)
- Preserved all deep content in 4 collapsed `<details>` blocks for engineers who want to dig in

## [0.6.25] - 2026-03-10

### Added
- "The Director's Eye" section between The Arc and Proof of Craft — 5-row table mapping film directing instincts (kill your darlings, 5-second rule, shoot coverage, direct the eye, calm ships) to concrete engineering decisions with cross-links to existing sections
- Bridges James's unique background (350+ music videos) to engineering craft in a way no generic dev profile can replicate — the section hiring managers remember when evaluating creative-technical leadership
- Updated audience routing table to direct hiring managers through The Director's Eye before Proof of Craft

## [0.6.24] - 2026-03-10

### Added
- "Technical DNA" subsection under Tech Stack between "Why These Tools" and GitHub Stats — 6-row pattern table (local-first, protocol over integration, fail at the boundary, observation masking, ship the feedback loop, composition over creation) each with definition and concrete evidence from shipped projects
- Surfaces the architectural instincts that connect individual tool choices into a coherent engineering philosophy — the systems-thinking layer hiring managers and senior engineers screen for
- Updated developer routing in "Reading This? Start Here" to include the new section

## [0.6.23] - 2026-03-10

### Added
- "How Passion Ships" section between How We Work and Engineering Principles — 5-phase ASCII pipeline diagram (Research → Strategize → Code → Analyze → Stage) showing what happens inside each 30-minute brain cycle, with collapsible deep-dive explaining memory persistence, LLM routing, subprocess isolation, feedback loops, and zero-intervention autonomy
- Turns the static architecture diagram into a dynamic workflow story — visitors now understand *how* the agent ships, not just *what* components exist
- Updated audience routing table to direct AI enthusiasts through the new section

## [0.6.22] - 2026-03-09

### Added
- "What I'd Build Differently" section between Hard Problems I've Solved and What's Next — 4 honest retrospectives on real architectural decisions: monolithic config at scale, raw SQL without a data access layer, unit-test-first coverage strategy, and component explosion vs composition patterns. Each includes what happened, what I'd change, and the transferable takeaway
- Signals senior-level self-awareness and growth mindset — the trait hiring managers screen for when they ask "tell me about a mistake you made"
- Updated developer routing in "Reading This? Start Here" to include the new section

## [0.6.21] - 2026-03-09

### Added
- "Recent Milestones" section between Currently Building and Latest From the Workshop — 4-entry chronological timeline (Dec 2025 → Mar 2026) showing verifiable shipped work with dates: Passionate Learning Suite completion, 190-release sprint, fcpxml-mcp-server traction, and Passion Agent's 1,000+ autonomous commits milestone
- Proves active momentum to recruiters who need to know "are they still shipping?" — each entry is date-stamped and verifiable against public repos
- Updated audience routing table to direct hiring managers through Recent Milestones first

## [0.6.20] - 2026-03-08

### Added
- "Hard Problems I've Solved" section between Proof of Craft and What's Next — 4 collapsible deep-dives into real engineering challenges: zero-denominator FCPXML parsing crashes, per-frame memory allocation in animation loops, context window management for autonomous agents, and iframe sandbox security for embedded dashboards. Each includes problem, approach, and measurable result
- Demonstrates technical depth and systems thinking — the section hiring managers use to differentiate tutorial-builders from production engineers

## [0.6.19] - 2026-03-08

### Added
- "Behind This README" collapsible section before Contribution Guidelines — documents the autonomous maintenance pipeline: auto-updated zones (daily status + workshop showcase) with marker conventions, branch naming patterns, the full subprocess agent pipeline from brain cycle to merge, and why automated README maintenance matters as proof of craft
- Turns the README into a self-referential portfolio piece — the page describes the system that maintains it

## [0.6.18] - 2026-03-08

### Added
- Glossary section after "How We Work" — collapsible table defining 10 ecosystem-specific terms (Brain Cycle, MCP, PACT, Passion Agent, Subprocess Agent, Somatic Markers, LLM Eval Suite, Intel Radar, Approval Rate, MCP Server) with linked references to repos and external docs
- Helps first-time visitors (especially hiring managers and developers) parse domain-specific terminology without breaking the main narrative flow

## [0.6.17] - 2026-03-08

### Security
- Added Security Policy section under Contribution Guidelines — severity-based reporting matrix (Critical/High → direct contact with 24h SLA, Medium/Low → GitHub security advisories), responsible disclosure commitments, and cross-repo security standards summary
- Strengthened Engineering Principles security row with specific OWASP Top 10 references (A03:2021 Injection, A05:2021 Security Misconfiguration) and linked to the new security policy

### Fixed
- Broken showcase URL: `TdotsSolutionsz Music Video Portfolio` had an unencoded space in the GitHub URL — replaced with correct repo slug `tdotssolutionsz-portfolio`

## [0.6.16] - 2026-03-08

### Added
- "Why These Tools" decision table under Tech Stack — 6 architecture decisions (Claude as primary LLM, Next.js 16 + React 19, SQLite over Postgres, MCP over custom APIs, Vitest over Jest, Vercel for everything) each with rationale and explicitly rejected alternatives
- Shows engineering judgment and tradeoff awareness, not just tool listing — the section hiring managers and senior engineers actually care about

## [0.6.15] - 2026-03-08

### Changed
- Metrics ribbon redesigned from inline-code wall to a 6-column stat card grid — each number (Gold Record, 350+ Videos, 29 Repos, 16+ Deployments, 1,257+ Commits, 24/7 Ecosystem) gets its own visual cell with label and subtitle for faster scanning
- Velocity metrics (190 releases, 60 brain cycles, 89.9% approval, 1,237+ tests) moved to compact `<sub>` line beneath the grid

### Added
- GitHub Profile Trophies widget (tokyonight theme, 6-column layout) at the top of the GitHub Stats section — adds social proof badges for commits, repos, stars, PRs, issues, and followers
- Two additional stat cards in GitHub Stats: "Commit Activity by Hour" (EST timezone) and "Most Used Languages by Commit" — shows when and what James ships, not just totals
- Footer signature line with Toronto location flag and Passion Agent attribution link

## [0.6.14] - 2026-03-06

### Added
- Hero tagline: "Gold-record music video director turned AI engineer" — gives cold visitors immediate context before the typing animation
- Velocity metrics ribbon below totals ribbon — surfaces the most impressive operational stats (190 releases/21 days, 60 brain cycles/day, 89.9% approval rate, 1,237+ tests) that were previously buried deep in the README
- Second closing thesis line: "The second best way is to watch their AI ship while they sleep" — reinforces the autonomous agent narrative

### Changed
- What's Next roadmap updated with specific technical details (Tailscale multi-machine, MCP beyond video editing) and current job search targets
- FOR_DARE.md Content Strategy Evolution updated with v0.6.14 entry

## [0.6.13] - 2026-03-06

### Added
- "Engineering Principles" section between How We Work and Open To — 6 values (ship-then-polish, accessibility, testing, security, open source, documentation) each paired with concrete "In Practice" evidence linking to shipped work
- FOR_DARE.md layout map updated to 20 sections (was 19), with Engineering Principles at position 10
- FOR_DARE.md Content Strategy Evolution updated with v0.6.13 entry

## [0.6.12] - 2026-03-06

### Added
- "Reading This? Start Here" audience-routing section after Project Goals — table directing hiring managers, developers, AI enthusiasts, and potential clients to the most relevant sections with deep links

### Fixed
- Broken anchor link in quick-nav bar: `#-all-28-projects` corrected to `#-all-29-projects` to match actual heading
- FOR_DARE.md Metrics Sync Map: updated all 4 stale metric references (module count 145+ → 92, LOC 46K+ → 109K, managed repos 36 → 47, public repos 28 → 29) with corrected approximate line numbers
- FOR_DARE.md Quick Reference, maintenance checklist, and Repo Count Accuracy section updated from 28 to 29 repos
- FOR_DARE.md Recruiter-Optimized Layout map updated to 19 sections (was 18), with corrected numbering and project count

## [0.6.11] - 2026-03-06

### Added
- Metrics Sync Map section in FOR_DARE.md — comprehensive cross-reference index mapping 7 hardcoded README metrics (commit count, public repos, module count, LOC, live deployments, managed repos, fcpxml stars) to their exact line numbers (37 total locations across 9 README sections), with source-of-truth references and a step-by-step update procedure

### Changed
- FOR_DARE.md Content Strategy Evolution updated with v0.6.11 entry

## [0.6.10] - 2026-03-06

### Added
- Design Language section in FOR_DARE.md — documents the README's visual system: 7-color palette with hex codes and usage rationale, badge style hierarchy (for-the-badge vs flat-square), 5 layout rules, and typography specifications
- Update Playbooks section in FOR_DARE.md — step-by-step procedures for 4 common maintenance operations: adding new repos, refreshing metrics, promoting featured projects, and seasonal content refreshes

### Changed
- FOR_DARE.md version history updated to include v0.6.10

## [0.6.9] - 2026-03-06

### Added
- Domain Depth section replacing flat specializations text line — visual Unicode bar chart showing expertise levels across 7 domains (AI Engineering, Autonomous Systems, Frontend, Creative Technology, Developer Tooling, Security Hardening, Infrastructure) with corresponding evidence
- What's Next section before Contribution Guidelines — forward-looking roadmap showing current focus, near-term plans, and career goal in tree-character format matching The Arc's visual style

### Changed
- Tech Stack section: specializations line removed in favor of the more informative Domain Depth chart
- README structure now has 18 distinct sections (was 16) for richer narrative

## [0.6.8] - 2026-03-05

### Changed
- Updated PACT Dashboard descriptions across 4 sections (Currently Building, Featured Projects, All Projects, architecture diagram) to reflect signal-based tab auto-selection, 7-binding global keyboard shortcut system with animated cheat sheet overlay, and iframe sandbox security hardening
- Strengthened Proof of Craft quality row with iframe sandboxing (OWASP A05:2021) and HTTPS-only origin validation evidence

## [0.6.7] - 2026-03-05

### Fixed
- ASCII diagram alignment in "How We Work" section: centered title text, fixed 3 lines with incorrect column width (2 short, 1 wide), ensuring all 34 box lines render at exactly 67 display columns
- Updated FOR_DARE.md version history to include v0.6.6 and v0.6.7

## [0.6.6] - 2026-03-05

### Added
- Vitest badge in tech stack reflecting adoption across ecosystem projects
- Vitest and API Security Hardening added to specializations list
- Testing evidence in Proof of Craft section: 45 Vitest tests (memory-master-mvp) and AbortController-hardened API layers

### Changed
- Updated memory-master-mvp description in All Projects to reflect premium micro-interactions, 45-test Vitest suite, and security-hardened fetch layer
- Proof of Craft quality row now cites specific security patterns (AbortController timeouts) alongside test counts

## [0.6.5] - 2026-03-05

### Added
- Quick Reference table at top of FOR_DARE.md — cheat sheet for common maintenance tasks (update counts, add projects, test changes)
- Dynamic Content Zones section documenting the two auto-updated README sections (daily status + showcase) with marker names, update frequency, and safe-editing rules
- Troubleshooting section covering 5 common issues: broken badges, stale stats cards, stale daily status, wrong counts, and GitHub rendering quirks
- Health check links in External Dependencies table for quick badge service verification

### Changed
- External Dependencies table now includes a Health Check column with clickable test URLs
- Updated FOR_DARE.md version history to include v0.6.5

## [0.6.4] - 2026-03-05

### Changed
- Synced FOR_DARE.md version history to cover v0.4.1 through v0.6.4 (was stuck at v0.4.1)
- Updated recruiter-optimized layout map from 10 sections to 16, matching current README structure (added Project Goals, Workshop Showcase, The Arc, Proof of Craft, Contribution Guidelines, metrics ribbon)
- Fixed stale repo count in maintenance checklist and Repo Count Accuracy section (16 → 28)

## [0.6.3] - 2026-02-25

### Changed
- Replaced flat Background comparison table with "The Arc" — a visual career timeline using tree characters that reads like a commit log, tracing the 2008→2026 journey from directing to engineering
- Rewrote closing CTA section: new quote, bold thesis statement ("evaluate an engineer by what they've shipped"), added third badge linking to passion.jamesdare.com
- Strengthened badge labels from generic ("See My Work", "Let's Talk") to action-oriented ("See Everything I've Built", "Let's Build Something", "Watch the Agent Work")

### Added
- "Proof of Craft" section with 5 verifiable claim→receipt pairs: MCP server, LLM eval suite sprint, agent commit count, client sites, test/quality metrics
- Each claim links to the actual evidence (repos, live deployments) so recruiters can verify without digging

## [0.6.2] - 2026-02-25

### Changed
- Updated all Passion Agent metrics to current state: 145+ modules, 46K+ LOC, 36 managed repos, 1,257+ total commits (previously showed 67+ modules, 30k+ LOC, 28 repos)
- Updated PACT Dashboard panel count from 28 to 30+ across all sections
- Updated "How We Work" architecture diagram with current repo count and commit totals
- Added Total Commits badge (1,257+) to hero badge bar and metrics ribbon
- Updated Background table with current module count and commit totals
- Updated "Open To" evidence table with commit count for shipping velocity proof
- Made casper-tng-website public with live link in All Projects section (was listed as private)

### Fixed
- Stale "394+ tests" metric replaced with more meaningful "1,257+ commits" across ecosystem
- Inconsistent repo count in architecture diagram (showed 28, ecosystem has 36)

## [0.6.1] - 2026-02-23

### Changed
- Showcase section updated to highlight TdotsSolutionsz portfolio's new design token system (5 RGB channel variables for alpha compositing) and parallax depth engine (4-layer spatial depth with lerp-smoothed rAF)
- Updated tdotssolutionsz-portfolio description in All Projects to reflect design tokens and parallax additions
- Added CSS Design Systems to Tech Stack specializations
- Showcase highlights now include accessibility notes (prefers-reduced-motion support) and codebase migration stats

## [0.6.0] - 2026-02-21

### Added
- Project Goals section articulating what drives every repo (AI tools, building in public, creative-technical bridge, autonomous collaboration)
- Contribution Guidelines section with fork workflow, conventional commits, and PR etiquette
- License, Repos, and Deployments badges in hero section for at-a-glance credibility
- Quick-navigation anchor links in Showcase section for jumping to Featured Projects, All Projects, Tech Stack, and How We Work

## [0.5.0] - 2026-02-18

### Changed
- Centered hero section with div alignment for magazine-style visual impact
- Added quick-glance metrics bar (gold record, repos, live deployments, agent status)
- Currently Building section now uses status table with 🟢/🟡 indicators
- Featured Projects restructured as 2×2 HTML table grid for visual weight
- All Projects section collapsed into `<details>` toggle to reduce scroll depth
- Open To section repositioned below How I Work for better narrative flow
- Closing CTA wrapped in centered div for consistent alignment

## [0.4.2] - 2026-02-09

### Added
- Contribution model section in FOR_DARE.md documenting Passion Agent workflow, branch conventions, valid task types, and PR review flow
- Two new maintenance checklist items: CHANGELOG version sequencing and FOR_DARE.md/CHANGELOG sync

### Changed
- Updated FOR_DARE.md version history to include v0.4.1 as current version

## [0.4.1] - 2026-02-08

### Changed
- Improved CHANGELOG with proper semver, full commit history, and Keep a Changelog format
- Updated FOR_DARE.md codebase map to include CHANGELOG.md
- Refreshed FOR_DARE.md version history and maintenance checklist to reflect current state

## [0.4.0] - 2026-02-08

### Added
- "How I Work" section with ASCII architecture diagram showing Passion Agent system
- Explains autonomous agent workflow: agent proposes improvements, owner reviews, agent learns

### Changed
- Sharpened Passion Agent descriptions to reflect multi-module architecture (orchestrator, learning engine, Discord bot, memory server)
- Updated Ultimate-Image-Video-Prompt-Generator description with current model support (Nano Banana, Veo3)
- Fixed orphaned Gemini badge in tech stack section (merged into AI & Infrastructure row)
- Updated branding, sharpened project descriptions, and added closing CTA

## [0.3.0] - 2026-02-08

### Added
- FOR_DARE.md project documentation
- Typing animation header via readme-typing-svg
- Upgraded all social badges to `for-the-badge` style

### Changed
- Reorganized tech stack into Languages & Frameworks / AI & Infrastructure categories

## [0.2.0] - 2026-02-07

### Added
- "Open To" section with evidence table for recruiter targeting
- Passion Agent as featured project (private, in active development)
- Live demo links on all deployed projects
- Promoted Vibe Coder to featured projects

### Changed
- Restructured entire README for recruiter scanning with proof-based value proposition

### Fixed
- Replaced broken `github-readme-streak-stats` badge with `profile-details` card
- Replaced unreliable `github-readme-stats` with `github-profile-summary-cards`

## [0.1.0] - 2026-02-06

### Added
- Profile view counter (komarev.com)
- Value proposition section
- "Currently Building" section with 3 active projects
- Star badges on featured project links
- Expanded featured section to 3 flagship projects with tech tags

### Fixed
- Repaired broken streak stats badge
- Added Anthropic to tech stack
- Removed duplicate project entries and fixed duplicate section emoji
- Fixed Passion Agent link

## [0.0.1] - 2026-02-05

### Added
- Visual badges, GitHub stats cards, and featured project section
- All 12 public repos organized by category
- Expanded tech stack with accurate framework/tool list

### Changed
- Merged visual overhaul with missing repos and expanded tech stack

## [0.0.0] - 2026-01-17

### Added
- Initial profile README
