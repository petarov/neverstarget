# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate README.md from README.md.template with the user's GitHub star lists.

Usage: GITHUB_TOKEN=... uv run build.py <login>
"""

import json
import os
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://api.github.com/graphql"
TEMPLATE = Path("README.md.template")
OUTPUT = Path("README.md")
PLACEHOLDER = "__STARRED__"
PAGE = 100

REPO_FIELDS = "__typename ... on Repository { nameWithOwner url description isArchived }"

LISTS_QUERY = f"""
query($login: String!, $after: String) {{
  user(login: $login) {{
    lists(first: {PAGE}, after: $after) {{
      pageInfo {{ hasNextPage endCursor }}
      nodes {{ id name description isPrivate }}
    }}
  }}
}}
"""

LIST_ITEMS_QUERY = f"""
query($id: ID!, $after: String) {{
  node(id: $id) {{
    ... on UserList {{
      items(first: {PAGE}, after: $after) {{
        pageInfo {{ hasNextPage endCursor }}
        nodes {{ {REPO_FIELDS} }}
      }}
    }}
  }}
}}
"""

STARS_QUERY = f"""
query($login: String!, $after: String) {{
  user(login: $login) {{
    starredRepositories(first: {PAGE}, after: $after) {{
      pageInfo {{ hasNextPage endCursor }}
      nodes {{ nameWithOwner url description isArchived }}
    }}
  }}
}}
"""


def graphql(token: str, query: str, variables: dict) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "readme-star-lists",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:500]
        raise RuntimeError(f"GitHub API HTTP {e.code}: {detail}") from e
    if payload.get("errors"):
        raise RuntimeError(f"GraphQL errors: {json.dumps(payload['errors'])}")
    return payload["data"]


def repos_only(nodes: list[dict]) -> list[dict]:
    return [n for n in nodes if n and n.get("__typename") == "Repository"]


def fetch_lists(token: str, login: str) -> list[dict]:
    lists = []
    after = None
    while True:
        data = graphql(token, LISTS_QUERY, {"login": login, "after": after})
        if data["user"] is None:
            raise RuntimeError(f"User not found: {login}")
        conn = data["user"]["lists"]
        for node in conn["nodes"]:
            if node["isPrivate"]:
                continue
            repos: list[dict] = []
            items_after = None
            more = True
            while more:
                page = graphql(token, LIST_ITEMS_QUERY, {"id": node["id"], "after": items_after})
                page_items = page["node"]["items"]
                repos.extend(repos_only(page_items["nodes"]))
                items_after = page_items["pageInfo"]["endCursor"]
                more = page_items["pageInfo"]["hasNextPage"]
            lists.append({"name": node["name"], "description": node["description"], "repos": repos})
        if not conn["pageInfo"]["hasNextPage"]:
            return lists
        after = conn["pageInfo"]["endCursor"]


def fetch_stars(token: str, login: str) -> list[dict]:
    stars = []
    after = None
    while True:
        data = graphql(token, STARS_QUERY, {"login": login, "after": after})
        conn = data["user"]["starredRepositories"]
        stars.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            return stars
        after = conn["pageInfo"]["endCursor"]


def one_line(text: str | None) -> str:
    return " ".join(text.split()) if text else ""


EMOJI_CATEGORIES = {"So", "Sk", "Cf"}  # symbols, skin-tone modifiers, ZWJ
VARIATION_SELECTORS = {"︎", "️"}


def sort_key(name: str) -> tuple[str, str]:
    stripped = "".join(
        c for c in name
        if unicodedata.category(c) not in EMOJI_CATEGORIES and c not in VARIATION_SELECTORS
    )
    return (" ".join(stripped.split()).casefold(), name.casefold())


def render_section(title: str, description: str | None, repos: list[dict]) -> list[str]:
    lines = [f"## {one_line(title)} ({len(repos)})", ""]
    desc = one_line(description)
    if desc:
        lines += [desc, ""]
    for repo in repos:
        entry = f"- **[{repo['nameWithOwner']}]({repo['url']})**"
        parts = []
        if repo.get("isArchived"):
            parts.append("**(archived)**")
        repo_desc = one_line(repo["description"])
        if repo_desc:
            parts.append(repo_desc)
        if parts:
            entry += " — " + " ".join(parts)
        lines.append(entry)
    lines.append("")
    return lines


def render(lists: list[dict], stars: list[dict]) -> str:
    lines: list[str] = []
    listed = set()
    for lst in sorted(lists, key=lambda l: sort_key(l["name"])):
        lines += render_section(lst["name"], lst["description"], lst["repos"])
        listed.update(r["nameWithOwner"] for r in lst["repos"])
    other = [r for r in stars if r["nameWithOwner"] not in listed]
    if other:
        lines += render_section("Other", None, other)
    return "\n".join(lines).rstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: uv run build.py <login>")
    login = sys.argv[1]
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")

    template = TEMPLATE.read_text(encoding="utf-8").splitlines()
    idx = [i for i, line in enumerate(template) if line.strip() == PLACEHOLDER]
    if len(idx) != 1:
        sys.exit(f"Expected exactly one '{PLACEHOLDER}' line in {TEMPLATE}, found {len(idx)}")

    block = render(fetch_lists(token, login), fetch_stars(token, login))
    i = idx[0]
    out = template[:i] + [block] + template[i + 1 :]
    OUTPUT.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
