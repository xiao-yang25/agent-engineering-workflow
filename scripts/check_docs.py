#!/usr/bin/env python3
"""Run the repository's offline checks for public documentation files."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


REPO_ROOT = Path(__file__).resolve().parent.parent

FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
FENCE_CLOSE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*$")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
EXPLICIT_ANCHOR_RE = re.compile(
    r"<a\s+[^>]*\b(?:id|name)\s*=\s*([\"'])([^\"']+)\1[^>]*>", re.IGNORECASE
)
LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
INLINE_CODE_RE = re.compile(r"(`+)(.*?)\1")

HOME_PATH_RULES = (
    (
        "personal-home-path-posix",
        re.compile(r"(?<![A-Za-z0-9])/(?:Users|home)/([^/\s`\"'<>]+)(?:/|$)"),
    ),
    (
        "personal-home-path-windows",
        re.compile(
            r"(?i)(?<![A-Za-z0-9])(?:[A-Z]:)?\\Users\\([^\\\s`\"'<>]+)\\"
        ),
    ),
)
PLACEHOLDER_USERS = {
    "user",
    "username",
    "your-user",
    "your_user",
    "yourname",
    "your-name",
    "your_name",
    "example-user",
    "example_user",
}

SECRET_RULES = (
    ("private-key-block", re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----")),
    ("aws-access-key-id", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,255}\b")),
    ("openai-api-key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("stripe-live-secret", re.compile(r"\bsk_live_[0-9A-Za-z]{16,}\b")),
)
CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?i)[\"']?(?:api[_-]?key|access[_-]?token|auth[_-]?token|"
    r"client[_-]?secret|password|passwd|aws_secret_access_key)[\"']?"
    r"\s*[:=]\s*[\"']?([^\s\"',;}]+)"
)
PLACEHOLDER_VALUES = {
    "changeme",
    "dummy",
    "example",
    "placeholder",
    "redacted",
    "replace-me",
    "replace_me",
    "secret",
    "your-token",
    "your_token",
}


@dataclass(frozen=True, order=True)
class Issue:
    path: str
    line: int
    rule: str
    detail: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.rule}: {self.detail}"


@dataclass
class MarkdownDocument:
    path: Path
    lines: list[str]
    anchors: set[str]
    links: list[tuple[int, str]]


def public_files() -> tuple[list[Path], list[Path], list[Issue]]:
    markdown: list[Path] = []
    json_files: list[Path] = []
    issues: list[Issue] = []
    for path in sorted(REPO_ROOT.glob("*.md")):
        if path.is_symlink():
            issues.append(Issue(path.name, 1, "public-symlink", "public file must not be a symlink"))
        elif path.is_file():
            markdown.append(path)

    for folder in ("docs", "examples"):
        directory_root = REPO_ROOT / folder
        if directory_root.is_symlink():
            issues.append(Issue(folder, 1, "public-symlink", "public directory must not be a symlink"))
            continue
        if not directory_root.is_dir():
            issues.append(Issue(folder, 1, "public-directory", "required public directory is missing"))
            continue
        pending = [directory_root]
        while pending:
            directory = pending.pop()
            for path in sorted(directory.iterdir()):
                if path.is_symlink():
                    issues.append(
                        Issue(relative(path), 1, "public-symlink", "public path must not be a symlink")
                    )
                elif path.is_dir():
                    pending.append(path)
                elif path.is_file() and path.suffix == ".md":
                    markdown.append(path)
                elif folder == "examples" and path.is_file() and path.suffix == ".json":
                    json_files.append(path)
    return sorted(markdown), sorted(json_files), issues


def relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def github_slug(title: str) -> str:
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"!?\[([^]]+)\]\([^)]*\)", r"\1", title)
    title = title.replace("`", "").strip().lower()
    chars: list[str] = []
    for char in title:
        category = unicodedata.category(char)
        if char in "-_" or char.isspace() or category[0] in {"L", "M", "N"}:
            chars.append(char)
    return re.sub(r"\s", "-", "".join(chars))


def parse_markdown(path: Path, text: str) -> tuple[MarkdownDocument, list[Issue]]:
    lines = text.splitlines()
    anchors: set[str] = set()
    links: list[tuple[int, str]] = []
    issues: list[Issue] = []
    heading_counts: dict[str, int] = {}
    fence: tuple[str, int, int] | None = None

    for number, line in enumerate(lines, start=1):
        if fence is not None:
            marker, minimum, _ = fence
            close_match = FENCE_CLOSE_RE.match(line)
            if close_match:
                candidate = close_match.group(1)
                if candidate[0] == marker and len(candidate) >= minimum:
                    fence = None
            continue
        open_match = FENCE_OPEN_RE.match(line)
        if open_match:
            marker = open_match.group(1)
            if marker[0] == "`" and "`" in open_match.group(2):
                continue
            fence = (marker[0], len(marker), number)
            continue

        for match in EXPLICIT_ANCHOR_RE.finditer(line):
            anchor = match.group(2)
            if anchor in anchors:
                issues.append(
                    Issue(relative(path), number, "duplicate-anchor", "anchor is defined more than once")
                )
            anchors.add(anchor)

        heading_match = HEADING_RE.match(line)
        if heading_match:
            base = github_slug(heading_match.group(2))
            if base:
                count = heading_counts.get(base, 0)
                anchor = base if count == 0 else f"{base}-{count}"
                heading_counts[base] = count + 1
                if anchor in anchors:
                    issues.append(
                        Issue(relative(path), number, "duplicate-anchor", "anchor is defined more than once")
                    )
                anchors.add(anchor)

        without_code = INLINE_CODE_RE.sub("", line)
        for match in LINK_RE.finditer(without_code):
            destination = extract_destination(match.group(1))
            if destination is not None:
                links.append((number, destination))

    if fence is not None:
        issues.append(
            Issue(relative(path), fence[2], "unclosed-fence", "fenced code block is not closed")
        )

    return MarkdownDocument(path, lines, anchors, links), issues


def extract_destination(raw: str) -> str | None:
    raw = raw.strip()
    if not raw:
        return None
    if raw.startswith("<"):
        end = raw.find(">")
        return raw[1:end] if end > 0 else raw[1:]
    return raw.split(maxsplit=1)[0]


def is_within_repo(path: Path) -> bool:
    try:
        path.relative_to(REPO_ROOT)
        return True
    except ValueError:
        return False


def check_link(
    document: MarkdownDocument,
    number: int,
    destination: str,
    documents: dict[Path, MarkdownDocument],
) -> Issue | None:
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc or destination.startswith("//"):
        return None

    link_path = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    if link_path:
        target = (
            REPO_ROOT / link_path.lstrip("/")
            if link_path.startswith("/")
            else document.path.parent / link_path
        ).resolve()
    else:
        target = document.path

    location = relative(document.path)
    if not is_within_repo(target):
        return Issue(location, number, "local-link", "target escapes the repository")
    if not target.exists():
        return Issue(location, number, "local-link", "target does not exist")
    if fragment:
        target_document = documents.get(target)
        if target_document is None:
            return Issue(location, number, "local-anchor", "fragment target is not a checked Markdown file")
        if fragment not in target_document.anchors:
            return Issue(location, number, "local-anchor", "fragment does not match a heading or explicit anchor")
    return None


def is_placeholder(value: str) -> bool:
    lowered = value.strip().lower()
    return (
        lowered in PLACEHOLDER_VALUES
        or lowered.startswith("$")
        or lowered.startswith("${")
        or (lowered.startswith("<") and lowered.endswith(">"))
        or lowered.startswith("your_")
        or lowered.startswith("your-")
    )


def check_sensitive_text(path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    location = relative(path)
    for rule, pattern in HOME_PATH_RULES:
        for match in pattern.finditer(text):
            if match.group(1).lower() not in PLACEHOLDER_USERS:
                issues.append(
                    Issue(location, line_number(text, match.start()), rule, "personal home path detected")
                )
    for rule, pattern in SECRET_RULES:
        for match in pattern.finditer(text):
            issues.append(
                Issue(location, line_number(text, match.start()), rule, "possible plaintext credential detected")
            )
    for match in CREDENTIAL_ASSIGNMENT_RE.finditer(text):
        if not is_placeholder(match.group(1)):
            issues.append(
                Issue(
                    location,
                    line_number(text, match.start()),
                    "credential-assignment",
                    "possible plaintext credential detected",
                )
            )
    return issues


def check_translations(documents: dict[Path, MarkdownDocument]) -> list[Issue]:
    """Check counterpart coverage and language switches, not translation quality."""
    pairs = [(REPO_ROOT / "README.md", REPO_ROOT / "README.en.md"),
             (REPO_ROOT / "AGENTS.md", REPO_ROOT / "docs/en/AGENTS.md")]
    pairs.extend((path, path.parent / "en" / path.name)
                 for path in sorted(documents)
                 if path.parent in (REPO_ROOT / "docs", REPO_ROOT / "examples"))
    issues: list[Issue] = []
    for chinese, english in pairs:
        for source, counterpart in ((chinese, english), (english, chinese)):
            document = documents.get(source)
            if document is None:
                issues.append(Issue(relative(source), 1, "translation-pair", "language counterpart is missing or unreadable"))
                continue
            if not any((source.parent / urlsplit(link).path).resolve() == counterpart
                       for _, link in document.links
                       if not urlsplit(link).scheme and not urlsplit(link).netloc):
                issues.append(Issue(relative(source), 1, "language-switch", "link to language counterpart is missing"))
    return issues


def comparable_config(value):
    """Ignore only human-facing role text when comparing localized examples."""
    result = json.loads(json.dumps(value))
    agents = result.get("agent") if isinstance(result, dict) else None
    if isinstance(agents, dict):
        for role in agents.values():
            if isinstance(role, dict):
                role.pop("description", None)
                role.pop("prompt", None)
    # Permission rule order can change which matching rule wins.
    return json.dumps(result, ensure_ascii=False)


def main() -> int:
    markdown_paths, json_paths, issues = public_files()
    documents: dict[Path, MarkdownDocument] = {}
    local_link_count = 0

    for path in markdown_paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            issues.append(Issue(relative(path), 1, "read-file", "file is not readable UTF-8 text"))
            continue
        document, markdown_issues = parse_markdown(path, text)
        documents[path.resolve()] = document
        issues.extend(markdown_issues)
        issues.extend(check_sensitive_text(path, text))

    issues.extend(check_translations(documents))

    for document in documents.values():
        for number, destination in document.links:
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or destination.startswith("//"):
                continue
            local_link_count += 1
            issue = check_link(document, number, destination, documents)
            if issue is not None:
                issues.append(issue)

    configurations = {}
    for path in json_paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            issues.append(Issue(relative(path), 1, "read-file", "file is not readable UTF-8 text"))
            continue
        issues.extend(check_sensitive_text(path, text))
        try:
            configurations[path] = json.loads(text)
        except json.JSONDecodeError as error:
            issues.append(Issue(relative(path), error.lineno, "json-syntax", "invalid JSON"))

    chinese_config = REPO_ROOT / "examples/opencode.json"
    english_config = REPO_ROOT / "examples/en/opencode.json"
    for path in (chinese_config, english_config):
        if path not in configurations:
            issues.append(Issue(relative(path), 1, "translation-pair", "localized JSON example is missing or invalid"))
    if chinese_config in configurations and english_config in configurations:
        if comparable_config(configurations[chinese_config]) != comparable_config(configurations[english_config]):
            issues.append(Issue(relative(english_config), 1, "configuration-parity", "localized examples differ beyond role descriptions and prompts"))

    if issues:
        for issue in sorted(set(issues)):
            print(issue.render(), file=sys.stderr)
        print(f"FAILED: {len(set(issues))} documentation issue(s)", file=sys.stderr)
        return 1

    print(
        f"OK: checked {len(markdown_paths)} Markdown file(s), "
        f"{len(json_paths)} JSON file(s), and {local_link_count} local link(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
