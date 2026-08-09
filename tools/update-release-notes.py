#!/usr/bin/env python3
"""Regenerate docs/telemffb/release-notes.md from TelemFFB's _RELEASE_NOTES.txt.

THE RELEASE PROCESS (docs side)
    1. A TelemFFB release is tagged on the app repo's `wip` branch, with its
       section in _RELEASE_NOTES.txt finalized (see banner format below).
    2. In this repo, run:      py tools/update-release-notes.py
       (fetches the txt from the app repo's wip branch; use --file to point
       at a local checkout instead).
    3. Review `git diff docs/telemffb/release-notes.md`, commit, push.
       The push to master triggers the deploy workflow, which publishes the
       site — no server access needed.

SOURCE FORMAT (_RELEASE_NOTES.txt in the app repo)
    Releases are delimited by banner lines of 10+ '#' characters, with a
    header line between them:

        ############################################
        ##  2.0.260807 - August 7, 2026
        ############################################

    The header is "<release-tag> - <display date>". Older sections that
    predate this convention carry only a date; their tags come from the
    frozen TAGMAP below (historical entries only — never extend it, put the
    tag in the txt banner instead).

    Within a section: "## Area" headers become bold labels, bullet lists
    pass through (indentation normalized), and "_ _" spacer lines become
    blanks.

OUTPUT CONTRACT
    - The page is GENERATED — hand edits are overwritten on the next run.
    - Newest release renders expanded with id="latest". The in-app update
      notification opens /telemffb/latest/, a stub that redirects to that
      anchor, so the newest section must always carry it (this script does).
    - No '##' markdown headings inside a release block: the site's
      enumerate-headings plugin would number them.
"""
import argparse
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "docs" / "telemffb" / "release-notes.md"
DEFAULT_URL = "https://raw.githubusercontent.com/walmis/VPforce-TelemFFB/wip/_RELEASE_NOTES.txt"

# Frozen tag mapping for historical sections whose txt banner carries only a
# date (pre-dating the "<tag> - <date>" banner convention). Do NOT extend
# this for new releases — put the tag in the txt banner instead.
TAGMAP = {
    "July 2026 - Draft":   ("2.0.260807", "August 7, 2026"),
    "October 29, 2025":    ("2.0.251029_p1", "October 29, 2025"),
    "October 7, 2025":     ("2.0.251007", "October 7, 2025"),
    "October 5, 2025":     ("2.0.100525", "October 5, 2025"),
    "May 6, 2025":         ("20250506", "May 6, 2025"),
    "March 9, 2025":       ("20250309", "March 9, 2025"),
    "January 1, 2025":     ("20250101", "January 1, 2025"),
    "December 13, 2024":   ("20241213", "December 13, 2024"),
    "November 3, 2024":    ("20241103", "November 3, 2024"),
    "October 31, 2024":    ("20241031", "October 31, 2024"),
    "October 6, 2024":     ("20241006", "October 6, 2024"),
    "September 8, 2024":   ("20240908", "September 8, 2024"),
    "August 11, 2024":     ("20240811", "August 11, 2024"),
    "July 26, 2024":       ("20240726", "July 26, 2024"),
    "July 5, 2024":        ("20240705", "July 5, 2024"),
    "June 22, 2024":       ("20240622", "June 22, 2024"),
    "June 5, 2024":        ("20240605", "June 5, 2024"),
    "May 26, 2024":        ("20240526", "May 24-26, 2024"),
}

BANNER = re.compile(r"^#{10,}\s*$", re.M)
HEADER = re.compile(r"^\s*#{1,4}\s*(.+?)\s*$")
BULLET = re.compile(r"^(\s*)-\s+(.*)$")
# "<tag> - <date>" banner: tag = leading token with no spaces, containing a digit
TAGGED_HEADER = re.compile(r"^(\S*\d\S*)\s+-\s+(.+)$")


def indent_level(n):
    # Source uses 1-3 spaces inconsistently for a first sub-level and 4+ for
    # a second. Bucket generously to avoid skipped-level (phantom) nesting.
    if n <= 0:
        return 0
    if n <= 3:
        return 1
    if n <= 5:
        return 2
    return 3


def convert_body(raw: str) -> str:
    out = []
    for line in raw.splitlines():
        if line.strip() in ("_ _", "_"):
            out.append("")
            continue
        m = BULLET.match(line)
        if m:
            lvl = indent_level(len(m.group(1)))
            out.append("    " * lvl + "- " + m.group(2).rstrip())
            continue
        h = HEADER.match(line)
        if h and not line.lstrip().startswith("-"):
            text = h.group(1).replace("\\", "/").rstrip(":")
            out.append("")
            out.append(f"**{text}**")
            out.append("")
            continue
        out.append(line.rstrip())
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n")
    return text


def resolve_header(date_raw: str):
    """Return (tag_or_None, display_date) for a section header."""
    if date_raw in TAGMAP:
        return TAGMAP[date_raw]
    m = TAGGED_HEADER.match(date_raw)
    if m:
        return m.group(1), m.group(2)
    return None, date_raw


def generate(src_text: str) -> str:
    parts = BANNER.split(src_text)
    # parts[0] = preamble; then alternating header, content, header, content...
    sections = []
    i = 1
    while i < len(parts):
        date_raw = parts[i].strip().lstrip("#").strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((date_raw, body))
        i += 2
    if not sections:
        sys.exit("No release sections found — is the source file valid?")

    blocks = []
    for idx, (date_raw, body) in enumerate(sections):
        tag, disp = resolve_header(date_raw)
        summary = f"{tag} &mdash; {disp}" if tag else disp
        body_md = convert_body(body)
        attrs = 'class="release" markdown="1"'
        if idx == 0:
            attrs = 'class="release release--latest" id="latest" markdown="1" open'
            summary += ' <span class="latest-badge">latest</span>'
        blocks.append(
            f'<details {attrs}>\n'
            f'<summary>{summary}</summary>\n\n'
            f'{body_md}\n'
            f'</details>'
        )

    header = (
        "<!--\n"
        "  GENERATED FILE - do not edit by hand; changes will be overwritten.\n"
        "  Regenerate with:  py tools/update-release-notes.py\n"
        "  (see that script's docstring for the release process and the\n"
        "  _RELEASE_NOTES.txt banner format)\n"
        "-->\n\n"
        "# TelemFFB Release Notes\n\n"
        "New, improved, and changed functionality for each TelemFFB release, "
        "newest first. This is a curated summary of user-facing changes &mdash; "
        "for the complete commit history see "
        "[GitHub](https://github.com/walmis/VPforce-TelemFFB).\n\n"
        "!!! tip\n"
        "    Version names match the release tag on the `wip` branch. The most "
        "recent release is expanded below; click any older version to expand it.\n"
    )
    return header + "\n" + "\n\n".join(blocks) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--file", type=Path, default=None,
                    help="Read _RELEASE_NOTES.txt from a local path instead "
                         "of fetching from the app repo's wip branch")
    ap.add_argument("--url", default=DEFAULT_URL,
                    help="Source URL when --file is not given")
    ap.add_argument("--force", action="store_true",
                    help="Allow regenerating even if it would remove the "
                         "page's current latest release")
    args = ap.parse_args()

    if args.file:
        src_text = args.file.read_text(encoding="utf-8")
        origin = str(args.file)
    else:
        with urllib.request.urlopen(args.url, timeout=15) as resp:
            src_text = resp.read().decode("utf-8")
        origin = args.url

    new_page = generate(src_text)

    # Safety: never silently REMOVE the page's current latest release. This
    # happens when the source lags the published page (e.g. regenerating
    # from `wip` while the newest release's notes only exist on a feature
    # branch that has not merged yet). Adding newer releases on top is fine.
    if OUT.exists() and not args.force:
        cur = re.search(r"<summary>(.*?)</summary>", OUT.read_text(encoding="utf-8"))
        # Strip the latest-badge span: once a newer release lands on top,
        # this entry legitimately appears in the new page without it.
        if cur:
            cur_summary = re.sub(r"\s*<span.*?</span>", "", cur.group(1)).strip()
        if cur and cur_summary not in new_page:
            sys.exit(
                f"REFUSING: the page's current latest release\n"
                f"    {cur.group(1)}\n"
                f"is not present in the source ({origin}) — the source is\n"
                f"probably behind the published page. Use --file to point at\n"
                f"the branch that has the newest notes, or --force to\n"
                f"regenerate anyway and drop that entry."
            )

    OUT.write_text(new_page, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.relative_to(REPO_ROOT)} ({new_page.count('<details')} releases) from {origin}")


if __name__ == "__main__":
    main()
