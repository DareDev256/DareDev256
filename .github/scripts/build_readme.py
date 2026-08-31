#!/usr/bin/env python3
"""Regenerate the DAILY_STATUS block in README.md from live GitHub data.

Three facts, each of which is only true today, and each of which the reader
can click through and check:

  1. the most recent release across every public non-fork repo, tag + ISO date
  2. the most recent public commit authored by DareDev256, repo + subject
  3. the current CI conclusion on fcp-mcp-server's default branch

Rules this script is built around:

  * It writes ONLY between <!-- DAILY_STATUS_START --> and
    <!-- DAILY_STATUS_END -->. Everything else in README.md is human-owned and
    is passed through byte for byte, markers included.
  * If a fact cannot be sourced, its column is dropped. If no fact can be
    sourced, the block is EMPTIED. A stale status line would be the one
    sentence on this page that contradicts the page.
  * Standard library only. No requirements.txt, no pip step, nothing to rot.

Exit codes: 0 = all three columns rendered. 3 = degraded (one or more columns
missing, possibly all). The workflow commits either way and only fails the job
when the block came out completely empty.
"""

import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

OWNER = "DareDev256"

# The profile repo is excluded from the "latest commit" search on purpose: this
# script commits to it, so including it would make the block cite its own last
# write, change every day for that reason alone, and say nothing.
SELF_REPO = "DareDev256"

CI_REPO = "fcp-mcp-server"

# Shown under the table so a reader can see what produced it and check the
# producer. It names THIS script and the date, and it deliberately does not
# promise a cadence. A cadence sentence is a claim about the future that the
# page cannot demonstrate: accurate the day it is typed, and visibly false the
# first fortnight the schedule does not fire. The date is the whole receipt. If
# it is stale, the reader can see that it is stale, which is the honest failure
# mode. The run schedule lives in build-readme.yml, where it cannot lie.
GENERATOR_URL = "https://github.com/{}/{}/blob/main/.github/scripts/build_readme.py".format(
    OWNER, SELF_REPO
)
GENERATOR_FILE = "build_readme.py"

ROOT = pathlib.Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

START = "<!-- DAILY_STATUS_START -->"
END = "<!-- DAILY_STATUS_END -->"

API = "https://api.github.com"
GRAPHQL = "https://api.github.com/graphql"

RETRYABLE = {429, 500, 502, 503, 504}
MAX_RETRIES = 4

# validate-readme.yml hard-fails the build if any of these land in README.md.
# A commit subject is untrusted text, so it gets checked before it is quoted.
SECRET_PATTERNS = re.compile(
    r"\bsk-[a-zA-Z0-9_-]{20,}|\bghp_[a-zA-Z0-9]{36,}|\bAKIA[A-Z0-9]{16,}"
    r"|\bBearer [a-zA-Z0-9._\-]{20,}"
)

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def warn(message):
    """Emit a GitHub Actions warning annotation, and a plain line locally."""
    print("::warning::{}".format(message) if os.environ.get("GITHUB_ACTIONS") else "WARN: " + message)


def request(url, data=None):
    """GET or POST the GitHub API, retrying transient gateway errors."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "daredev256-build-readme",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    body = json.dumps(data).encode() if data is not None else None
    if body is not None:
        headers["Content-Type"] = "application/json"

    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(url, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as error:
            if error.code not in RETRYABLE or attempt == MAX_RETRIES - 1:
                raise
            warn("GitHub returned {} for {}, retrying".format(error.code, url))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            if attempt == MAX_RETRIES - 1:
                raise
            warn("network error on {}: {}, retrying".format(url, error))
        time.sleep(2 ** attempt)


REPOS_QUERY = """
query($owner: String!) {
  user(login: $owner) {
    repositories(first: 100, privacy: PUBLIC, isFork: false,
                 ownerAffiliations: OWNER,
                 orderBy: {field: PUSHED_AT, direction: DESC}) {
      nodes {
        name
        url
        isArchived
        defaultBranchRef {
          target {
            ... on Commit {
              abbreviatedOid
              messageHeadline
              committedDate
              url
              author { user { login } }
            }
          }
        }
        releases(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
          nodes { tagName publishedAt url isDraft isPrerelease }
        }
      }
    }
  }
}
"""


def fetch_repos():
    payload = request(GRAPHQL, {"query": REPOS_QUERY, "variables": {"owner": OWNER}})
    if payload.get("errors"):
        raise RuntimeError("GraphQL errors: {}".format(payload["errors"]))
    nodes = payload["data"]["user"]["repositories"]["nodes"]
    return [repo for repo in nodes if not repo["isArchived"]]


def day(iso):
    """2026-08-31T04:04:32Z -> 2026-08-31."""
    return iso.split("T")[0]


def clean_subject(text):
    """Quote a commit subject safely: one line, no table pipes, no em-dash, short.

    Truncation at the first em-dash is deliberate. Owner rule: no em-dashes in
    prose on this page. Cutting a quotation short with an ellipsis is honest;
    rewriting someone's commit message is not.
    """
    text = " ".join(text.split())
    if SECRET_PATTERNS.search(text):
        return None
    for dash in ("—", "–"):
        if dash in text:
            text = text.split(dash)[0].rstrip() + "…"
            break
    if len(text) > 72:
        text = text[:71].rstrip() + "…"
    return text.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def latest_release(repos):
    candidates = []
    for repo in repos:
        for release in repo["releases"]["nodes"]:
            if release["isDraft"] or release["isPrerelease"]:
                continue
            if not release["publishedAt"]:
                continue
            candidates.append((release["publishedAt"], repo, release))
    if not candidates:
        return None
    published, repo, release = max(candidates, key=lambda row: row[0])
    return {
        "header": "Latest release",
        "cell": "[{repo} `{tag}`]({url})<br><sub>{date}</sub>".format(
            repo=repo["name"], tag=release["tagName"], url=release["url"],
            date=day(published),
        ),
    }


def latest_commit(repos):
    candidates = []
    for repo in repos:
        if repo["name"] == SELF_REPO:
            continue
        ref = repo["defaultBranchRef"]
        commit = ref and ref.get("target")
        if not commit or not commit.get("committedDate"):
            continue
        author = ((commit.get("author") or {}).get("user") or {}).get("login")
        if author != OWNER:
            continue
        subject = clean_subject(commit["messageHeadline"] or "")
        if not subject:
            continue
        candidates.append((commit["committedDate"], repo, commit, subject))
    if not candidates:
        return None
    committed, repo, commit, subject = max(candidates, key=lambda row: row[0])
    return {
        "header": "Latest commit",
        "cell": "[{repo} `{oid}`]({url}) {subject}<br><sub>{date}</sub>".format(
            repo=repo["name"], oid=commit["abbreviatedOid"], url=commit["url"],
            subject=subject, date=day(committed),
        ),
    }


def ci_status():
    url = "{}/repos/{}/{}/actions/runs?branch=main&status=completed&per_page=1".format(
        API, OWNER, CI_REPO
    )
    runs = request(url).get("workflow_runs") or []
    if not runs:
        return None
    run = runs[0]
    conclusion = run.get("conclusion")
    if not conclusion:
        return None
    mark = {"success": "passing", "failure": "failing"}.get(conclusion, conclusion)
    return {
        "header": "{} CI".format(CI_REPO),
        "cell": "[{name}: {mark}]({url})<br><sub>{date}</sub>".format(
            name=run.get("name") or "CI", mark=mark, url=run["html_url"],
            date=day(run["created_at"]),
        ),
    }


def render(columns):
    """A single-row table plus a provenance line.

    No columns means no table AND no provenance line: the block goes empty. A
    "generated today" stamp under an empty table would be the page asserting
    freshness it just failed to source.
    """
    if not columns:
        return ""
    header = "| " + " | ".join(column["header"] for column in columns) + " |"
    rule = "|" + "|".join([" --- "] * len(columns)) + "|"
    row = "| " + " | ".join(column["cell"] for column in columns) + " |"
    stamp = "<sub>Generated {date} from the GitHub API by [{file}]({url}).</sub>".format(
        date=time.strftime("%Y-%m-%d", time.gmtime()),
        file=GENERATOR_FILE, url=GENERATOR_URL,
    )
    return "\n".join([header, rule, row, "", stamp])


def write_block(body):
    content = README.read_text()
    pattern = re.compile(
        "{}.*?{}".format(re.escape(START), re.escape(END)), re.DOTALL
    )
    if not pattern.search(content):
        raise RuntimeError("DAILY_STATUS markers not found in README.md")
    inner = "\n{}\n".format(body) if body else "\n"
    updated = pattern.sub(lambda _: START + inner + END, content, count=1)
    if updated != content:
        README.write_text(updated)
    return updated


def main():
    columns = []
    try:
        repos = fetch_repos()
    except Exception as error:
        warn("repo scan failed, dropping release and commit columns: {}".format(error))
        repos = []

    if repos:
        for builder in (latest_release, latest_commit):
            try:
                column = builder(repos)
            except Exception as error:
                warn("{} failed: {}".format(builder.__name__, error))
                column = None
            if column:
                columns.append(column)
            else:
                warn("{} produced nothing, column dropped".format(builder.__name__))

    try:
        column = ci_status()
    except Exception as error:
        warn("ci_status failed: {}".format(error))
        column = None
    if column:
        columns.append(column)
    else:
        warn("ci_status produced nothing, column dropped")

    body = render(columns)
    write_block(body)

    print("--- generated block ---")
    print(body if body else "(empty)")
    print("--- end ---")
    print("{}/3 columns sourced".format(len(columns)))

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as handle:
            handle.write("### DAILY_STATUS: {}/3 columns sourced\n\n".format(len(columns)))
            handle.write(body + "\n" if body else "_Block emptied: nothing could be sourced._\n")

    return 0 if len(columns) == 3 else 3


if __name__ == "__main__":
    sys.exit(main())
