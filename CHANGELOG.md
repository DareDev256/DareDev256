# Changelog

All notable changes to the DareDev256 GitHub profile README are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/): major = full redesign, minor = new sections, patch = fixes/updates.

## [Unreleased]

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
