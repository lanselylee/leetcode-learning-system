#!/usr/bin/env python3
"""Create a solution note and add it to the review schedule."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


TOPIC_DIRS = {
    "array": "array",
    "two-pointers": "array",
    "hash-map": "hash-map",
    "backtracking": "backtracking",
    "dp": "dp",
    "dynamic-programming": "dp",
    "greedy": "greedy",
    "binary-search": "binary-search",
    "tree": "tree",
    "stack": "stack",
    "queue": "queue",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def solution_template(problem_id: int, title: str, topic: str) -> str:
    return f'''"""
LeetCode: {problem_id}. {title}
Approach: {topic}
Link: https://leetcode.com/problems/{slugify(title).replace("_", "-")}/
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    pass


# Notes:
# - Intuition:
# - Edge cases:
# - Mistakes:
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new LeetCode solution file and review item.")
    parser.add_argument("problem_id", type=int)
    parser.add_argument("title")
    parser.add_argument("--difficulty", default="Medium", choices=["Easy", "Medium", "Hard"])
    parser.add_argument("--topic", required=True)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    topic_key = args.topic.lower().replace(" ", "-")
    topic_dir = TOPIC_DIRS.get(topic_key, slugify(args.topic))
    relative_path = Path("solutions") / topic_dir / f"{args.problem_id}_{slugify(args.title)}.py"
    solution_path = ROOT / relative_path

    if solution_path.exists() and not args.overwrite:
        raise SystemExit(f"{relative_path} already exists. Use --overwrite to replace it.")

    solution_path.parent.mkdir(parents=True, exist_ok=True)
    solution_path.write_text(solution_template(args.problem_id, args.title, args.topic), encoding="utf-8")

    subprocess.run(
        [
            "python3",
            str(ROOT / "scripts" / "review.py"),
            "add",
            str(args.problem_id),
            args.title,
            "--difficulty",
            args.difficulty,
            "--topic",
            args.topic,
            "--path",
            str(relative_path),
        ],
        check=True,
        cwd=ROOT,
    )
    print(f"Created {relative_path}")


if __name__ == "__main__":
    main()
