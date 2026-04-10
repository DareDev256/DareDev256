# Changelog

All notable changes to the DareDev256 GitHub profile README are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/): major = full redesign, minor = new sections, patch = fixes/updates.

## [Unreleased]

## [0.8.61] - 2026-04-10

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: README.md ~35KB → ~37KB, CHANGELOG.md ~62KB → ~64KB (9th recurrence of file-size drift)

### Changed
- **README.md** — Expanded Repo Setup "How It Works" paragraph to describe the CI pipeline's 5 validation checks (line count, marker integrity, version chain, SVG presence, secret scanning) instead of the previous generic "CI validates README constraints" one-liner
- **README.md** — Added `.github/workflows/validate-readme.yml` to the file inventory table (5 files → 6 files) — the CI pipeline was added at v0.8.58 but never documented in the repo file listing
- **README.md** — Added CI validation row to Security Model table documenting secret-scan patterns and structural drift prevention (CWE-798)
- **CLAUDE.md** — Version bump v0.8.60 → v0.8.61

## [0.8.60] - 2026-04-09

### Changed
- **README.md** — Updated PACT Dashboard descriptions across 4 locations (Currently Building, Featured Projects, ecosystem diagram, All Projects) to document the new Auto-Select toggle: `useAutoSelect` hook manages enabled/disabled state with localStorage persistence, toggle component gates the scoring pipeline so manual browsing bypasses curation, and panel data updates dynamically with animated transitions when toggled
- **README.md** — Expanded auto-selection engine entry in Hard Problems to document the user-facing toggle architecture, hook design (`useAutoSelect`), and panel data behavior on mode switch

## [0.8.59] - 2026-04-08

### Fixed
- **CI Pipeline** — Secret scanning regex `sk-[a-zA-Z0-9]` false-positived on `task-type` in FOR_DARE.md. Tightened all patterns to require 16-20+ character matches using extended regex (`grep -E`), eliminating false positives while still catching real API keys

## [0.8.58] - 2026-04-08

### Added
- **CI Pipeline** — GitHub Actions workflow (`.github/workflows/validate-readme.yml`) that validates README line count, auto-update marker integrity, marker zone ordering, version consistency between CHANGELOG and CLAUDE.md, signature.svg presence, and secret scanning on every push/PR to main

### Fixed
- **CI** — Repo had no CI pipeline — added automated validation to catch recurring drift bugs (file-size drift, missing markers, version mismatches) before they ship

## [0.8.57] - 2026-04-08

### Changed
- **README.md** — Updated PACT Dashboard descriptions across 4 locations (Currently Building, Featured Projects, ecosystem diagram, All Projects) to document tier-visual feedback system: `getTierVisuals` translates combo tiers into distinct retro-arcade visual styles (colors, glow intensities, label treatments), communicating scoring state visually
- **README.md** — Expanded auto-selection engine entry in Hard Problems to document `getTierVisuals` utility and its role in the visual feedback loop

### Fixed
- **README.md** — Stale file size in Repo Setup table: FOR_DARE.md ~60KB → ~61KB (8th recurrence of file-size drift)
- **CLAUDE.md** — Version bump v0.8.56 → v0.8.57

## [0.8.56] - 2026-04-08

### Added
- **FOR_DARE.md** — Table of Contents with 15-entry navigation index (section → description → anchor links) — the 57KB reference file had no way to jump to sections without searching
- **FOR_DARE.md** — Automated validation script in Maintenance Checklist section — a `bash validate.sh` one-liner that checks version chain consistency, Content Strategy "(current)" marker, showcase URL spaces, and README line count. Catches the 4 most common recurring bugs (10+ Content Strategy drifts, 7+ file-size drifts, 5+ showcase URL breaks) before they ship

## [0.8.55] - 2026-04-08

### Fixed
- **FOR_DARE.md** — Content Strategy Evolution stuck at v0.8.53 "(current)" — missing v0.8.54 entry (10th recurrence of Content Strategy drift: v0.8.0, v0.8.3, v0.8.15, v0.8.31, v0.8.37, v0.8.42, v0.8.46, v0.8.53, v0.8.55)
- **FOR_DARE.md** — Version Milestones table missing v0.8.54 and v0.8.55 entries
- **FOR_DARE.md** — Recurring Bug Summary: Content Strategy drift count 9+ → 10+, added v0.8.55 to version list
- **CLAUDE.md** — Version bump v0.8.54 → v0.8.55

## [0.8.54] - 2026-04-07

### Changed
- **README.md** — Updated PACT Dashboard descriptions across 4 locations (Currently Building, Featured Projects, ecosystem diagram, All Projects) to reflect current feature set: System Matrix grid, Intel/Ops dual-panel layout, live Threat Level indicator, and persistent Session Clock
- **CLAUDE.md** — Version bump v0.8.53 → v0.8.54

## [0.8.53] - 2026-04-06

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: README.md ~34KB → ~35KB, FOR_DARE.md ~55KB → ~57KB, CHANGELOG.md ~60KB → ~62KB (7th recurrence of file-size drift)
- **FOR_DARE.md** — Content Strategy Evolution stuck at v0.8.50 "(current)" — synced through v0.8.53 with entries for v0.8.51, v0.8.52, v0.8.53 (9th recurrence of Content Strategy drift)
- **FOR_DARE.md** — Version Milestones table missing entries for v0.8.51, v0.8.52, v0.8.53
- **FOR_DARE.md** — Recurring Bug Summary stale counts: file-size drift 4 → 7 (missing v0.8.51, v0.8.52, v0.8.53), Content Strategy drift 8+ → 9+
- **CLAUDE.md** — Version bump v0.8.52 → v0.8.53

## [0.8.52] - 2026-04-06

### Added
- **README.md** — Cache TTL column in External Services table: documents badge refresh intervals (Shields.io ~5min, stats cards ~6hrs, komarev real-time) plus GitHub camo proxy caching note for troubleshooting stale badges
- **README.md** — Commit Conventions subsection in Repo Setup: documents prefix vocabulary (`docs:`, `fix:`, `feat:`, `refactor:`, `chore:`), version bump rules, and the 3-file version chain invariant

### Fixed
- **README.md** — Stale file size in Repo Setup table: CHANGELOG.md ~59KB → ~60KB (6th recurrence of file-size drift)
- **CLAUDE.md** — Version bump v0.8.51 → v0.8.52

## [0.8.51] - 2026-04-06

### Changed
- **README.md** — Improved setup instructions: added prerequisites note, clarified case-sensitive repo naming requirement, expanded local preview options (branch preview URL)
- **README.md** — Auto-Update API docs: marker format now shows full HTML comment syntax (`<!-- DAILY_STATUS_START -->`) instead of shorthand, added showcase zone extraction example alongside existing daily status example, moved idempotency note into the integration callout
- **README.md** — Added color palette contract reference (`#6C63FF`/`#A78BFA`/`#818CF8`) to Security Model section footer for cross-file discoverability

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: FOR_DARE.md ~57KB→~55KB, CHANGELOG.md ~60KB→~59KB (5th recurrence of file-size drift)
- **CLAUDE.md** — Version bump v0.8.50 → v0.8.51

## [0.8.50] - 2026-04-05

### Changed
- **README.md** — Sharpened PACT Dashboard descriptions across 4 locations (Currently Building, Featured Projects, ecosystem diagram, All Projects) — each now has context-appropriate depth instead of repeating the full auto-select implementation details everywhere. Improved scannability for recruiters
- **README.md** — Tightened Hard Problems entries: auto-selection engine and envelope sanitization entries condensed without losing technical substance

### Fixed
- **README.md** — Stale file size in Repo Setup table: FOR_DARE.md listed as ~54KB (actual ~55KB)
- **CLAUDE.md** — Version bump v0.8.49 → v0.8.50

## [0.8.49] - 2026-04-05

### Fixed
- **README.md** — Recurring broken showcase URL (5th occurrence: v0.6.17, v0.8.10, v0.8.32, v0.8.47, v0.8.49): literal spaces in GitHub repo slug `TdotsSolutionsz Music Video Portfolio` → corrected to `tdotssolutionsz-portfolio`

### Added
- **FOR_DARE.md** — New Recurring Bug Summary table in Troubleshooting section: surfaces the 4 most frequent recurring bugs (showcase URL spaces ×5, file-size drift ×4, Content Strategy drift ×8+, Hard Problems count drift ×7+) with occurrence counts, affected versions, root causes, and prevention steps
- **FOR_DARE.md** — Added v0.8.49 to Content Strategy Evolution with "(current)" marker
- **FOR_DARE.md** — Added v0.8.49 to Version Milestones table
- **FOR_DARE.md** — Updated showcase URL troubleshooting recurrence history (4→5 occurrences)

### Changed
- **CLAUDE.md** — Version bump v0.8.48 → v0.8.49

## [0.8.48] - 2026-04-04

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: README.md ~34KB→~35KB, CHANGELOG.md ~57KB→~59KB, FOR_DARE.md ~51KB→~54KB (4th recurrence of file-size drift: v0.8.38, v0.8.43, v0.8.46, v0.8.48)

### Added
- **FOR_DARE.md** — New troubleshooting entry: "File sizes in Repo Setup drift from actual (RECURRING)" — documents the recurring pattern, fix procedure, and prevention steps
- **FOR_DARE.md** — Added file size consistency check to Maintenance Checklist
- **FOR_DARE.md** — Added v0.8.47 and v0.8.48 to Version Milestones table
- **FOR_DARE.md** — Added v0.8.48 to Content Strategy Evolution with "(current)" marker

### Changed
- **CLAUDE.md** — Version bump v0.8.47 → v0.8.48

## [0.8.47] - 2026-04-04

### Fixed
- **README.md** — Recurring broken showcase URL (4th occurrence: v0.6.17, v0.8.10, v0.8.32, v0.8.47): literal spaces in GitHub repo slug `TdotsSolutionsz Music Video Portfolio` → corrected to `tdotssolutionsz-portfolio`
- **FOR_DARE.md** — Updated troubleshooting recurrence history for showcase URL bug (3→4 occurrences), synced Content Strategy through v0.8.47

### Changed
- **CLAUDE.md** — Version bump v0.8.46 → v0.8.47

## [0.8.46] - 2026-04-04

### Added
- **README.md** — Scannable index at top of "Hard Problems I've Solved" details block: 16 entries categorized by domain (Parsing & Data, Performance, Architecture, Security, UX Engineering, Testing) with one-liner labels for recruiter scanning

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: README.md ~32KB→~34KB, CHANGELOG.md ~54KB→~57KB, FOR_DARE.md ~50KB→~51KB
- **FOR_DARE.md** — Content Strategy Evolution stuck at v0.8.44 "(current)", missing v0.8.45 entry (8th recurrence of recurring drift). Added v0.8.45 + v0.8.46 entries, moved "(current)" marker
- **FOR_DARE.md** — Version Milestones table missing v0.8.46 entry

### Changed
- **CLAUDE.md** — Version bump v0.8.45 → v0.8.46

## [0.8.45] - 2026-04-03

### Changed
- **README.md** — Enhanced auto-select engine descriptions across all 5 locations (Currently Building, Featured Projects, All Projects catalog, Ecosystem diagram, Hard Problems) to articulate UX value: "eliminates manual task hunting" with animated focus transitions and guided data exploration
- **README.md** — Added WCAG accessibility callout (OWASP-hardened → OWASP-hardened, WCAG-accessible) to PACT Dashboard descriptions and `aria-live` region documentation in Hard Problems entry
- **CLAUDE.md** — Version bump v0.8.44 → v0.8.45

## [0.8.44] - 2026-04-02

### Added
- **README.md** — New Hard Problems entry: "Spring-physics gauge needle in SVG" — documents MomentumGauge spring-based animation loop (`stiffness × (target - current) - damping × velocity`) with ref-only state to avoid re-render thrash
- **README.md** — New Hard Problems entry: "Comprehensive `auto_at_intervals` test coverage" — documents unit test suite covering interval scheduling, edge cases (zero-length timelines, single-frame clips), error handling within callbacks, and cancellation cleanup. JSDoc annotations added for full IDE support

### Changed
- **README.md** — Updated PACT Dashboard descriptions across 4 locations (Currently Building, Featured Projects, All Projects catalog, Ecosystem diagram) to reflect spring-physics MomentumGauge SVG needle
- **CLAUDE.md** — Version bump v0.8.43 → v0.8.44

## [0.8.43] - 2026-04-02

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: README.md listed as ~30KB (actual ~32KB), CHANGELOG.md listed as ~52KB (actual ~54KB)
- **FOR_DARE.md** — Hard Problems count in Patterns Worth Stealing still said "11 deep-dive war stories" despite v0.8.42 claiming this fix — actual count is 14 (7th recurrence of count drift). Updated to 14
- **FOR_DARE.md** — Troubleshooting recurrence history for Hard Problems count drift was stale: only listed v0.8.16 and v0.8.25, missing v0.8.42 incomplete fix

### Changed
- **FOR_DARE.md** — Added v0.8.43 to Content Strategy Evolution and Version Milestones
- **CLAUDE.md** — Version bump v0.8.42 → v0.8.43

## [0.8.42] - 2026-04-02

### Fixed
- **FOR_DARE.md** — Content Strategy Evolution stuck at v0.8.38 "(current)", missing v0.8.39–v0.8.41 entries (6th occurrence of recurring drift — previously fixed at v0.8.0, v0.8.3, v0.8.15, v0.8.31, v0.8.37). Added 4 entries, moved "(current)" marker to v0.8.42
- **FOR_DARE.md** — Hard Problems entry count stale in Maintenance Checklist: listed as 11, actual count is 14 (missed additions at v0.8.24, v0.8.26, v0.8.30)
- **CLAUDE.md** — Stale collapsed section reference: "All 33 Projects" → "All 34 Projects" (repo count bumped at v0.8.39, CLAUDE.md never synced)

### Changed
- **FOR_DARE.md** — Added v0.8.38 and v0.8.42 to Version Milestones quick-reference table
- **CLAUDE.md** — Version bump v0.8.41 → v0.8.42

## [0.8.41] - 2026-04-02

### Added
- **README.md** — New Hard Problems entry: "SSE invalidation starvation under rapid agent cycles" — documents hybrid throttle-debounce replacement (300ms trailing + 1.5s max-wait ceiling) and abort-signal guards on `usePassionAPI` fetch parsing that eliminated stale UI data

### Changed
- **README.md** — Updated PACT Dashboard descriptions (Currently Building + Featured Projects) to reflect SSE invalidation hardening and `useIntersectionObserver` hook adoption
- **CLAUDE.md** — Version bump v0.8.40 → v0.8.41

## [0.8.40] - 2026-04-01

### Added
- **README.md** — New Hard Problems entry: "Silent marker loss from duplicate clip names" — documents `auto_at_intervals` bug where name-only clip lookup caused silent marker overwrites; fixed with `(clip_name, clip_index)` tuple keying
- **README.md** — New Hard Problems entry: "Duplicated observer setup across components" — documents extraction of `useIntersectionObserver` hook from 4 redundant `IntersectionObserver` implementations across PACT components

### Changed
- **CLAUDE.md** — Version bump v0.8.39 → v0.8.40

## [0.8.39] - 2026-04-01

### Added
- **README.md** — Added Website repo (jamesdare.com portfolio) to Client Websites in All Projects catalog — was referenced in showcase but missing from the project list

### Changed
- **README.md** — Bumped public repo count 33 → 34 across all 3 locations (hero badge, Open To table, All Projects header) per Metrics Sync Map
- **CLAUDE.md** — Version bump v0.8.38 → v0.8.39, updated project count reference in size cap rules

## [0.8.38] - 2026-03-31

### Fixed
- **README.md** — Stale file sizes in Repo Setup table: FOR_DARE.md listed as ~48KB (actual ~50KB), CHANGELOG.md listed as ~49KB (actual ~51KB)

### Added
- **README.md** — Accessibility row in Security Model table: documents `role="img"`, `aria-label`, `<title>`, `<desc>` on signature.svg and `alt` text on all badge images, linked to WCAG 1.1.1
- **signature.svg** — Class→phase quick-reference map in header comment: maps all 8 CSS class groups (`.inf`, `.ob`, `.el`, `.nc`, `.wr-*`, `.sk`, `.arr`, `.nm`/`.sub`/`.tag`) to their animation phases for targeted edits
- **FOR_DARE.md** — Content Strategy Evolution entry for v0.8.38

### Changed
- **CLAUDE.md** — Version bump v0.8.37 → v0.8.38

## [0.8.37] - 2026-03-31

### Fixed
- **FOR_DARE.md** — Content Strategy Evolution stuck at v0.8.35 "(current)", missing v0.8.36 entry (5th occurrence of recurring drift — previously fixed at v0.8.0, v0.8.3, v0.8.15, v0.8.31). Added v0.8.36 and v0.8.37 entries, moved "(current)" marker

### Added
- **FOR_DARE.md** — New Troubleshooting entry: "Hard Problems count drifts from actual entries (RECURRING)" — documents v0.8.16 and v0.8.25 recurrence history, fix procedure, and prevention pattern
- **FOR_DARE.md** — Maintenance Checklist: added Hard Problems entry count consistency check (currently 11)

### Changed
- **CLAUDE.md** — Version bump v0.8.36 → v0.8.37

## [0.8.36] - 2026-03-30

### Changed
- **README.md** — Detailed the auto-select engine across all 5 reference points (Currently Building, Featured Projects, ecosystem diagram, All 33 Projects, Hard Problems): expanded from bare "auto-select engine" label to describe viewport-aware scoring, interaction signal tracking, and content adjacency ranking — the actual engineering behind the feature
- **README.md** — Sharpened Hard Problems auto-select entry: reframed from "video embeds" to the general-purpose scoring engine it became, added dwell time as an interaction signal, emphasized deterministic testability of the rules layer

## [0.8.35] - 2026-03-30

### Fixed
- **README.md** — Removed duplicate 3-column table header from file inventory in Repo Setup section — stale remnant from pre-v0.8.34 header upgrade caused malformed table rendering on GitHub (3-column header + 4-column data rows)
- **FOR_DARE.md** — Fixed 3 stale Metrics Sync Map context strings: PACT Component Count Featured Projects entry had period instead of comma (`121 components. 695 tests` → `121 components, 695 tests`); PACT Test Count Featured Projects and All 33 Projects entries used reversed phrasing (`695 tests, OWASP-hardened` → `OWASP-hardened. 121 components, 695 tests`) to match actual README text

### Changed
- **CLAUDE.md** — Version bump v0.8.34 → v0.8.35

## [0.8.34] - 2026-03-30

### Changed
- **README.md** — Enhanced Repo Setup documentation: added file sizes to inventory table, added `prefers-color-scheme` light-mode customization note to replication step 3, added concrete `curl | sed` one-liner for auto-update zone polling, linked all CWE references in Security Model table to mitre.org entries for verifiability

## [0.8.33] - 2026-03-30

### Changed
- **README.md** — Tightened Repo Setup & Dependencies section: clearer replication instructions (added badge instance count, SVG center coordinate reference), merged redundant Auto-Update API tables into single format table, sharpened Security Model threat descriptions. Total 395→388 lines (−7)
- **README.md** — Improved file inventory table: added zero-JS note for SVG, distinguished internal docs from design docs, linked Passion Agent to live URL in architecture description

## [0.8.32] - 2026-03-30

### Fixed
- **README.md** — Recurring broken showcase URL (3rd occurrence: v0.6.17, v0.8.10, v0.8.32): Passion Agent wrote `TdotsSolutionsz Music Video Portfolio` with literal spaces in GitHub URL — guaranteed 404. Corrected to hyphenated slug `tdotssolutionsz-portfolio`

### Added
- **FOR_DARE.md** — Content Strategy Evolution: added v0.8.32 entry, marked as current
- **FOR_DARE.md** — Troubleshooting: added prevention pattern (grep one-liner) to Showcase URL section — catches spaces in repo slugs before they ship. Documented this as 3rd recurrence with version history

### Changed
- **CLAUDE.md** — Version bump v0.8.31 → v0.8.32

## [0.8.31] - 2026-03-29

### Fixed
- **FOR_DARE.md** — Content Strategy Evolution drift: stuck at v0.8.25 "(current)", missing 5 entries (v0.8.26–v0.8.30). Added all missing entries with accurate summaries from CHANGELOG
- **FOR_DARE.md** — Stale Metrics Sync Map context: PACT Component Count ecosystem diagram row still referenced "Royalty Protocol hero" (removed in v0.8.28). Updated to match current README text
- **FOR_DARE.md** — "What I'd Build Differently" count drift: listed 4 retrospectives but README has 5 (Learning Suite entry added in v0.8.29). Corrected to 5

### Added
- **FOR_DARE.md** — Version Milestones: added v0.8.27 (SVG security hardening) and v0.8.30 (parallax engine showcase) rows

### Changed
- **CLAUDE.md** — Version bump v0.8.30 → v0.8.31

## [0.8.30] - 2026-03-29

### Added
- **README.md** — New showcase: passion-site v3.53.0 parallax engine — 4-layer wheel-driven scroll parallax, ambient sine-wave drift, momentum decay with return-to-center
- **README.md** — Two new "Hard Problems" entries: wheel-driven parallax engine (depth-factor mapping, CSS custom property offsets, single rAF loop) and enum aliasing flake in test suite (`MarkerType.INCOMPLETE`/`TODO` identity vs value assertion)

### Changed
- **CLAUDE.md** — Version bump v0.8.29 → v0.8.30

## [0.8.29] - 2026-03-28

### Fixed
- **README.md** — PACT Dashboard description drift: 3 of 4 locations still used "Cyberpunk command terminal" / "Cyberpunk HUD" after v0.8.28 standardized Currently Building to "Agent command terminal". Unified all 4 instances (Featured Projects, All 33 Projects, ecosystem diagram) to match recruiter-scannable framing
- **README.md** — Ecosystem diagram was missing "695 tests" for PACT Dashboard — the only location that omitted the test count metric after v0.8.28 added it elsewhere

### Changed
- **README.md** — Learning Suite description in Currently Building: replaced implementation details ("polished loading states, guarded engine startup") with curriculum topics ("prompt engineering, red teaming, bias detection, hallucination hunting") — what recruiters scan for
- **README.md** — New "What I'd Build Differently" entry: Learning Suite shared layout — 10 games with identical shells built independently, reflecting on the speed-vs-architecture tradeoff
- **CLAUDE.md** — Version bump v0.8.28 → v0.8.29

## [0.8.28] - 2026-03-28

### Changed
- **README.md** — Tightened PACT Dashboard descriptions across 4 locations (Currently Building, Featured Projects, All 33 Projects, ecosystem diagram): cut cosmetic feature names (Purple Reign, Royalty Protocol, BaseModal, NavLink, IntelDossier) to surface what recruiters scan for (capabilities, test count, security posture)
- **README.md** — Condensed Auto-Update API documentation: merged verbose format examples and 5-row field reference table into a single scannable zone-format table with inline field descriptions. Cuts 19 lines while preserving all integration details
- **README.md** — Total line count reduced 408 → 389 (back under 400 cap)
- **CLAUDE.md** — Version bump v0.8.27 → v0.8.28

## [0.8.27] - 2026-03-27

### Security
- **signature.svg** — Hardened root `<svg>` element: added `role="img"`, `aria-label`, `<title>`, `<desc>` for non-interactive semantics. Added security constraints comment block documenting forbidden patterns (`<script>`, `<foreignObject>`, `on*` handlers, `url()`, `@import`, external refs) — mitigates CWE-79 (XSS via SVG injection) and CWE-918 (SSRF via external resource loading)
- **README.md** — Added Security Model table inside Repo Setup section documenting SVG hardening, auto-update zone boundaries, and external badge isolation strategy

## [0.8.26] - 2026-03-27

### Added
- **README.md** — New "Hard Problems" entry: SSE data layer extraction — `useSSEConnection` refactored into focused `useSSE` hook with typed `{data, error, isLoading}` state and first-class loading/error UI

### Changed
- **README.md** — PACT Dashboard descriptions updated across 4 locations (Currently Building, Featured Projects, All 33 Projects, ecosystem diagram) to reflect `useSSE` streaming architecture
- **FOR_DARE.md** — Hard Problems count 8 → 9
- **CLAUDE.md** — Version bump v0.8.25 → v0.8.26

## [0.8.25] - 2026-03-27

### Fixed
- **signature.svg** — Stale header comment: "Subtitle text must match 'Open To' roles" contradicted CLAUDE.md v0.8.22 fix. Subtitles are brand identity titles, not job targets. Corrected to match the established constraint
- **FOR_DARE.md** — Hard Problems count drift: listed "7 deep-dive war stories" but README has 8 entries after the v0.8.24 async cleanup addition. Updated to 8

### Added
- **FOR_DARE.md** — Version Milestones: added v0.8.24 row (React hooks cleanup, SVG instruction sharpening)
- **FOR_DARE.md** — Content Strategy Evolution: synced through v0.8.24, added v0.8.25 entry as current

### Changed
- **CLAUDE.md** — Version bump v0.8.24 → v0.8.25

## [0.8.24] - 2026-03-27

### Added
- **README.md** — New "Hard Problems" entry: async cleanup in React animation hooks — documented `useIdleAnimations`/`useTerminal`/`useSSEConnection` timer leak fixes using ref-based unmount guards

### Changed
- **README.md** — Repo Setup replication instructions: sharpened step 3 (explicit hex values + element classes) and step 5 (added GFM renderer alternative to `grip`)

## [0.8.23] - 2026-03-26

### Added
- **FOR_DARE.md** — File Cross-References & Editability map: dependency graph showing how all 5 files reference each other, with editability matrix and breakage risk ratings per file
- **FOR_DARE.md** — Pre-Push Quick Check: condensed 5-item fast-path checklist for Passion Agent's rapid iteration cycles (version chain, metric consistency, Content Strategy sync, showcase URL, line count)
- **README.md** — "How It Works" architecture summary in Repo Setup collapsed section — explains the zero-build-step rendering pipeline and agent write zones in two sentences

### Changed
- **FOR_DARE.md** — Content Strategy Evolution synced through v0.8.22, added v0.8.23 entry
- **CLAUDE.md** — Version bump v0.8.22 → v0.8.23

## [0.8.22] - 2026-03-26

### Fixed
- **CLAUDE.md** — SVG subtitle constraint was misleading: said subtitles "must match role titles in Open To section" but subtitles are brand identity titles (what James *is*), not job targets (what he's *seeking*). Clarified to prevent future agents from "fixing" intentional divergence
- **README.md** — Repo Setup replication step 3 referenced nonexistent `:root` CSS variables and was vague about which `<text>` elements to edit. Now cites exact class names (`sub`, `tag`) and specific hex values

### Added
- **FOR_DARE.md** — Metric Verification Commands: one-liner shell commands for checking each of the 13 Sync Map metrics against their source of truth (GitHub API, tokei, jq, vitest). Includes rate-limit note for unauthenticated GitHub API calls
- **FOR_DARE.md** — Troubleshooting entry for recurring Content Strategy Evolution drift (stuck at old version) — documented pattern across v0.7.1, v0.8.2, v0.8.14 with fix procedure
- **FOR_DARE.md** — Version Milestones: added v0.8.21 row (MCP-native era)
- **FOR_DARE.md** — Content Strategy Evolution: synced through v0.8.22

### Changed
- **CLAUDE.md** — Version bump v0.8.21 → v0.8.22

## [0.8.21] - 2026-03-26

### Added
- **README.md** — MCP Protocol badge in Tech Stack section — MCP is a core differentiator missing from the badge grid
- **README.md** — "MCP & Integrations" domain added to Domain Depth expertise chart (protocol design, tool registries, memory servers)
- **README.md** — "MCP-native architecture" pattern added to Technical DNA table — documents protocol-first approach across ecosystem
- **README.md** — Proof of Craft MCP claim expanded to cite both `fcpxml-mcp-server` and `passion-memory-server`

### Changed
- **README.md** — Featured Projects grid: replaced `passion-site` (static HTML site) with `passion-memory-server` (MCP server powering the ecosystem) — stronger technical proof for the portfolio
- **FOR_DARE.md** — Content Strategy Evolution synced through v0.8.20, added v0.8.21 entry
- **CLAUDE.md** — Version bump v0.8.20 → v0.8.21

## [0.8.20] - 2026-03-26

### Changed
- **README.md** — PACT Dashboard descriptions updated across 4 locations (Currently Building, Featured Projects, All 33 Projects, ecosystem diagram) to reflect auto-select engine — viewport-aware embed selection with `computeEntryTiming`, `freezeActivityMap`, `maxSeverity` rules
- **README.md** — Proof of Craft quality claim updated: "OWASP-hardened throughout" → "OWASP Top 10 security audit, input validation at every boundary" — reflects the deep security audit across passion-agent
- **README.md** — Auto-Update API docs: added raw endpoint URL, clarified propagation timing, improved integration note for external consumers

### Added
- **CLAUDE.md** — version bump v0.8.19 → v0.8.20

## [0.8.19] - 2026-03-25

### Fixed
- **FOR_DARE.md** — Layout map section count: "9 visible + 6 collapsed" → 8 visible — the showcase zone is embedded within Currently Building via HTML comment markers, not a standalone section. Previous count inflated the visible section number since v0.7.2
- **FOR_DARE.md** — Content Strategy Evolution: stuck at v0.8.17 as "(current)", missing v0.8.18 entry — now synced through v0.8.19

### Added
- **FOR_DARE.md** — Version Milestones quick-reference table: 9-row summary of the 52-entry Content Strategy arc — shows the growth→trim→stabilize pattern (peak 760 lines at v0.6.0, trimmed to 301 at v0.7.0, steady ~390 since)
- **FOR_DARE.md** — Clarifying note under layout map explaining that daily status and showcase zones are embedded within Currently Building, not standalone sections
- **CLAUDE.md** — Version bump v0.8.18 → v0.8.19

## [0.8.18] - 2026-03-24

### Changed
- **README.md** — PACT Dashboard descriptions updated across 5 locations (Currently Building, Featured Projects, All 33 Projects, ecosystem diagram, showcase zone) to reflect Purple Reign intro sequence — pulsating purple aura, metallic sheen title reveal, dark luxury aesthetic
- **README.md** — Showcase zone updated with Purple Reign + BaseModal refactor + NavLink component as latest notable build

### Added
- **README.md** — BaseModal architecture and NavLink navigation component documented in PACT Dashboard descriptions — centralized modal logic and animated sidebar navigation
- **CLAUDE.md** — version bump v0.8.17 → v0.8.18

## [0.8.17] - 2026-03-24

### Added
- **FOR_DARE.md** — Metrics Sync Map: 4 new metrics tracked — PACT Component Count (`121`, 5 locations), Approval Rate (`89.9%`, 4 locations), PACT Test Count (`695`, 4 locations), fcpxml Tool Count (`53`, 2 locations). Total tracked metrics now 13 (was 9)
- **FOR_DARE.md** — Quick Reference: added entries for bumping component count and approval rate (the two most frequently drifting new metrics)
- **FOR_DARE.md** — Maintenance Checklist: added Sync Map completeness check (all 13 metrics consistent across documented locations)
- **FOR_DARE.md** — Content Strategy Evolution: synced through v0.8.17

## [0.8.16] - 2026-03-24

### Fixed
- **FOR_DARE.md** — Hard Problems count: "6 deep-dive war stories" → 7 (cinematic hero orchestration was added in v0.8.15 but count wasn't bumped)
- **README.md** — Repo Setup editability matrix: CHANGELOG.md listed as "Human only" but agents write to it every version — corrected to "Human + Agent"

### Added
- **FOR_DARE.md** — Metrics Sync Map: added ecosystem test count (`1,400+`, 2 locations) and release velocity (`190`, 2 locations) — both metrics appear in multiple README sections but were missing from the sync map, risking stale-number drift

## [0.8.15] - 2026-03-23

### Changed
- **README.md** — PACT Dashboard descriptions updated across 5 locations (Currently Building, Featured Projects, All 33 Projects, ecosystem diagram, showcase zone) to reflect Royalty Protocol hero — dynamic background video, scroll-triggered reveals, dark luxury tech aesthetic
- **README.md** — Showcase zone updated with Royalty Protocol as latest notable build, layered on IntelDossier + smart video embeds

### Added
- **README.md** — New Hard Problems entry: cinematic hero orchestration (staggered reveal choreography, lazy video loading, IntersectionObserver-driven sequences, zero layout shift)
- **FOR_DARE.md** — Content Strategy Evolution synced through v0.8.15 (was stuck at v0.8.13 as "current", missing v0.8.14 entry)

## [0.8.14] - 2026-03-23

### Added
- **README.md** — IntelDossier feature documented across Currently Building, Featured Projects, All 33 Projects, and ecosystem diagram — animated threat indicators, tiered severity bars, source analysis panel
- **README.md** — Intelligent video embed auto-selection documented in Hard Problems I've Solved — viewport-aware selection engine replacing simultaneous iframe loading

### Changed
- **README.md** — PACT Dashboard descriptions updated across 4 locations to reflect IntelDossier hero section and smart video embeds
- **README.md** — Showcase zone updated with IntelDossier + smart video embeds as latest notable build
- **CLAUDE.md** — version bump v0.8.13 → v0.8.14

## [0.8.13] - 2026-03-23

### Fixed
- **FOR_DARE.md** — Design Language color palette: Orchid hex was `#A855F7` (never used anywhere) — corrected to `#A78BFA` to match actual signature.svg secondary color; updated usage description to reflect real SVG element usage (subtitles, arrows, electrons, nucleus ring)

### Added
- **signature.svg** — Self-documenting header block: color contract, 8-phase animation sequence, dimension/theme specs, edit safety notes — eliminates dependency on FOR_DARE.md for developers opening the SVG directly

### Changed
- **CLAUDE.md** — version bump v0.8.12 → v0.8.13

## [0.8.12] - 2026-03-23

### Fixed
- **FOR_DARE.md** — Content Strategy Evolution: stuck at v0.8.10 as "(current)", missing v0.8.11 entry — now synced through v0.8.12

### Added
- **FOR_DARE.md** — Troubleshooting: new "Showcase URL has broken link (RECURRING)" entry documenting the twice-hit URL encoding bug (v0.6.17, v0.8.10) with root cause, history, and long-term fix guidance
- **FOR_DARE.md** — Maintenance Checklist: added showcase URL validation check (the exact thing that keeps breaking) and Content Strategy sync verification

### Changed
- **CLAUDE.md** — version bump v0.8.11 → v0.8.12

## [0.8.11] - 2026-03-22

### Fixed
- **README.md** — All 33 Projects: added 2 missing entries (`passion-memory-server`, `DareDev256` profile repo) — list now actually contains 33 projects matching header count

### Added
- **README.md** — Auto-Update API: field reference table documenting every dynamic field (task count, repo count, line diff, success rate, showcase repo) with format, source, and semantic meaning
- **README.md** — Auto-Update API: integration note with raw file URL for machine-readable status consumption

### Changed
- **CLAUDE.md** — version bump v0.8.10 → v0.8.11

## [0.8.10] - 2026-03-21

### Fixed
- **README.md** — Showcase zone: broken GitHub URL with unencoded spaces in repo slug (`TdotsSolutionsz Music Video Portfolio` → `tdotssolutionsz-portfolio`) — same bug previously fixed in v0.6.17, re-introduced by Passion Agent auto-update

### Changed
- **CLAUDE.md** — version bump v0.8.9 → v0.8.10

## [0.8.9] - 2026-03-21

### Fixed
- **FOR_DARE.md** — Patterns Worth Stealing: All Projects claimed "5 category tables" but README only has 4 (AI & Automation, Passionate Learning Suite, Interactive Web & Games, Client Websites) — corrected count
- **FOR_DARE.md** — Content Strategy Evolution: synced through v0.8.9, was stuck at v0.8.8 as "(current)"

### Changed
- **CLAUDE.md** — version bump v0.8.8 → v0.8.9

## [0.8.8] - 2026-03-20

### Fixed
- **FOR_DARE.md** — Troubleshooting: commit count reference still said "4" after Metrics Sync Map was corrected to 3 in v0.8.6 — now consistent
- **FOR_DARE.md** — Content Strategy Evolution: was stuck at v0.8.6 as "(current)", missing v0.8.7 entry — now synced through v0.8.8

### Added
- **FOR_DARE.md** — Signature SVG Architecture: full documentation of the 8-phase animation sequence, timing table, color contract, theme-switch behavior, and edit safety notes for the `signature.svg` hero emblem

### Changed
- **CLAUDE.md** — version bump v0.8.7 → v0.8.8

## [0.8.7] - 2026-03-19

### Changed
- **Repo Setup & Dependencies** — file inventory table now shows "Editable By" column (Human only vs Human + Agent) to prevent accidental edits in machine-writable zones
- **External Services table** — added "Impact if Down" column with severity ratings (High/Medium/Low) for triage when badge services break
- **Auto-Update API** — added expected output format templates for both Daily Status and Showcase zones with exact field patterns, replacing vague "format specs in FOR_DARE.md" reference
- **Auto-Update API** — added source module name (`passion-profile.mjs`) to zone table so contributors can trace generation logic
- **Replication guide** — step 3 now specifies where to edit signature.svg (color variables, subtitle `<text>` elements, tagline stats); step 5 adds verification URL pattern and local preview with `grip`
- **CLAUDE.md** — version bump v0.8.6 → v0.8.7

## [0.8.6] - 2026-03-19

### Fixed
- **FOR_DARE.md** — Metrics Sync Map: commit count claimed 4 locations but only 3 exist (removed phantom "How the Passion Ecosystem" entry that never contained the commit number)
- **FOR_DARE.md** — Metrics Sync Map: managed repos listed "Featured Projects" as a location, but Featured Projects doesn't mention 47 — replaced with actual 4th location (All 33 Projects table)
- **FOR_DARE.md** — Metrics Sync Map: module count listed 4 locations but missed "What I'd Build Differently" (`config.json at 92 modules`) — now correctly shows 5
- **FOR_DARE.md** — Quick Reference: commit count "appears in 4 places" → corrected to 3
- **FOR_DARE.md** — Metrics Refresh playbook: "commit count appears in ~6 places" → corrected to 3 with cross-reference to Sync Map
- **FOR_DARE.md** — All Metrics Sync Map entries now include exact context strings (the surrounding text where each number appears) instead of vague section references — eliminates guesswork during updates

### Changed
- **FOR_DARE.md** — Content Strategy Evolution: added v0.8.6 entry, marked as current
- **CLAUDE.md** — version bump v0.8.5 → v0.8.6

## [0.8.5] - 2026-03-19

### Changed
- **Repo Setup & Dependencies** — restructured from wall-of-text into three clear subsections: numbered replication steps, file inventory table (README.md, signature.svg, CLAUDE.md, FOR_DARE.md, CHANGELOG.md with purpose), and auto-update API reference table (zone names, markers, frequency, content format)
- External services table now shows badge instance count (~25) for impact awareness when Shields.io goes down
- **FOR_DARE.md** — synced Content Strategy Evolution with v0.8.4 entry (was marked as current at v0.8.3)
- **CLAUDE.md** — version bump v0.8.4 → v0.8.5

## [0.8.4] - 2026-03-19

### Fixed
- **FOR_DARE.md** — added missing v0.8.3 entry to Content Strategy Evolution (was stuck at v0.8.2 as "current")
- **FOR_DARE.md** — corrected Patterns Worth Stealing section count: was "12 visible + 4 collapsed" (stale v0.7.0 snapshot), now reflects current 9+6 structure
- **FOR_DARE.md** — fixed Hard Problems count in collapsed sections list: 5 → 6 (envelope sanitization entry was added in v0.8.2 but count not bumped)

### Changed
- **CLAUDE.md** — version bump v0.8.3 → v0.8.4

## [0.8.3] - 2026-03-18

### Fixed
- **FOR_DARE.md** — synced Content Strategy Evolution through v0.8.2 (was stuck at v0.7.9 as "current"), adding 3 missing version entries (v0.8.0–v0.8.2)
- **FOR_DARE.md** — removed stale references to deleted sections ("What's Next", "The Arc") from Seasonal Content Refresh playbook — both cut in v0.7.0
- **FOR_DARE.md** — fixed stale example numbers in Troubleshooting (was "28 repos but you have 30", now reflects current 33+ range)
- **FOR_DARE.md** — corrected Metrics Sync Map: commit badge line reference, removed stale "The Arc" phrasing guidance
- **FOR_DARE.md** — fixed Maintenance Checklist deployment count (5 → 20+)

### Changed
- **CLAUDE.md** — version bump v0.8.2 → v0.8.3

## [0.8.2] - 2026-03-17

### Changed
- **Ecosystem test total** — bumped 1,374+ → 1,400+ across Open To and Proof of Craft sections
- **Showcase zone** — updated to PACT Dashboard envelope sanitizer: defense-in-depth structural pre-validation for YouTube API responses, CWE-20/CWE-400/CWE-754 coverage, +23 tests

### Added
- **Hard Problems I've Solved** — new entry: envelope sanitization at API boundaries (structural pre-validator before per-field processing)

## [0.8.1] - 2026-03-15

### Changed
- **Currently Building** — Passionate Learning Suite description updated to reflect UX polish: loading states, guarded engine startup
- **Repo Setup & Dependencies** — restructured from wall-of-text paragraphs to developer-friendly numbered setup steps, external services health check table, and auto-update API zone reference with marker names and frequencies
- **Passion Ecosystem** — added Passion Memory MCP link to "What makes this different" summary
- **CLAUDE.md** — version bump v0.8.0 → v0.8.1

## [0.8.0] - 2026-03-15

### Fixed
- **FOR_DARE.md** — synced Content Strategy Evolution through v0.7.9 (was stuck at v0.7.1 as "current"), adding 8 missing version entries
- **FOR_DARE.md** — fixed stale "typing SVG" references in Color Palette and Typography sections to match actual `signature.svg` implementation (replaced in v0.7.0)
- **FOR_DARE.md** — updated collapsed sections list: added Domain Depth + Technical DNA and Repo Setup & Dependencies (both missing), corrected Hard Problems count from 4 → 5, updated structure count 9+4 → 9+6
- **CLAUDE.md** — added missing "Domain Depth + Technical DNA" to collapsed sections list
- **CLAUDE.md** — version bump v0.7.9 → v0.8.0

## [0.7.9] - 2026-03-15

### Changed
- **Showcase zone** — updated to Passionate Learning Suite play page polish: visual loading spinner for engine initialization, refactored startup sequence guarding against race conditions for stable game state
- **CLAUDE.md** — version bump v0.7.8 → v0.7.9

## [0.7.8] - 2026-03-15

### Added
- **README.md** — new collapsed "Repo Setup & Dependencies" section: fork instructions, external service inventory with health check links, auto-update zone API documentation
- README now self-documents its own architecture for developers who want to replicate the profile pattern

### Changed
- **CLAUDE.md** — version bump v0.7.7 → v0.7.8

## [0.7.7] - 2026-03-13

### Fixed
- **CLAUDE.md** — added missing type definition for `signature.svg` asset: dimensions, color palette, animation contract, theme support, and sync constraints with README badges/titles
- **CLAUDE.md** — updated stale version reference from v0.7.0 to v0.7.7

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
