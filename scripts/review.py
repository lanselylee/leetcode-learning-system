#!/usr/bin/env python3
"""Manage a lightweight spaced repetition queue for LeetCode notes."""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEDULE_PATH = ROOT / "data" / "review_schedule.json"


def today() -> date:
    return date.today()


def parse_day(value: str) -> date:
    return date.fromisoformat(value)


def load_schedule() -> dict[str, Any]:
    if not SCHEDULE_PATH.exists():
        return {"version": 1, "intervals_days": [1, 3, 7, 14, 30, 60], "problems": []}
    return json.loads(SCHEDULE_PATH.read_text(encoding="utf-8"))


def save_schedule(schedule: dict[str, Any]) -> None:
    SCHEDULE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SCHEDULE_PATH.write_text(json.dumps(schedule, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def find_problem(schedule: dict[str, Any], problem_id: int) -> dict[str, Any] | None:
    for problem in schedule["problems"]:
        if int(problem["id"]) == problem_id:
            return problem
    return None


def next_interval(schedule: dict[str, Any], review_count: int, result: str) -> int:
    intervals = schedule.get("intervals_days", [1, 3, 7, 14, 30, 60])
    if result == "again":
        return 1
    if result == "hard":
        return 3
    index = min(review_count, len(intervals) - 1)
    days = int(intervals[index])
    if result == "easy":
        return max(days, 7)
    return days


def due_problems(schedule: dict[str, Any], target_day: date) -> list[dict[str, Any]]:
    due = []
    for problem in schedule["problems"]:
        if parse_day(problem["next_review"]) <= target_day:
            due.append(problem)
    return sorted(due, key=lambda item: (item["next_review"], int(item["id"])))


def format_problem(problem: dict[str, Any]) -> str:
    path = problem.get("path", "")
    location = f" ({path})" if path else ""
    return f"- #{problem['id']} {problem['title']} [{problem['topic']}, {problem['difficulty']}]{location}"


def command_add(args: argparse.Namespace) -> None:
    schedule = load_schedule()
    existing = find_problem(schedule, args.problem_id)
    current_day = today().isoformat()
    if existing:
        existing.update(
            {
                "title": args.title,
                "difficulty": args.difficulty,
                "topic": args.topic,
                "path": args.path,
            }
        )
        existing.setdefault("history", []).append({"date": current_day, "event": "updated"})
        print(f"Updated #{args.problem_id} {args.title}")
    else:
        schedule["problems"].append(
            {
                "id": args.problem_id,
                "title": args.title,
                "difficulty": args.difficulty,
                "topic": args.topic,
                "path": args.path,
                "last_reviewed": current_day,
                "next_review": (today() + timedelta(days=1)).isoformat(),
                "review_count": 0,
                "history": [{"date": current_day, "event": "added"}],
            }
        )
        print(f"Added #{args.problem_id} {args.title}; first review is tomorrow.")
    save_schedule(schedule)


def command_due(args: argparse.Namespace) -> None:
    schedule = load_schedule()
    target_day = parse_day(args.date) if args.date else today()
    due = due_problems(schedule, target_day)
    if not due:
        print(f"No reviews due by {target_day.isoformat()}.")
        return
    print(f"Reviews due by {target_day.isoformat()}:")
    for problem in due:
        print(format_problem(problem))


def command_review(args: argparse.Namespace) -> None:
    schedule = load_schedule()
    problem = find_problem(schedule, args.problem_id)
    if not problem:
        raise SystemExit(f"Problem #{args.problem_id} is not in the review schedule.")

    current_day = today()
    if args.result in {"good", "easy"}:
        problem["review_count"] = int(problem.get("review_count", 0)) + 1
    elif args.result == "again":
        problem["review_count"] = 0

    interval = next_interval(schedule, int(problem.get("review_count", 0)), args.result)
    problem["last_reviewed"] = current_day.isoformat()
    problem["next_review"] = (current_day + timedelta(days=interval)).isoformat()
    problem.setdefault("history", []).append(
        {
            "date": current_day.isoformat(),
            "event": "reviewed",
            "result": args.result,
            "next_review": problem["next_review"],
        }
    )
    save_schedule(schedule)
    print(f"Reviewed #{problem['id']} {problem['title']} as {args.result}.")
    print(f"Next review: {problem['next_review']}")


def command_github_output(args: argparse.Namespace) -> None:
    schedule = load_schedule()
    due = due_problems(schedule, today())
    output_path = Path(args.output)
    if not due:
        output_path.write_text("has_due=false\n", encoding="utf-8")
        print("No due reviews.")
        return

    body = ["## Reviews due today", ""]
    body.extend(format_problem(problem) for problem in due)
    body.extend(["", "Run `python3 scripts/review.py review <id> --result good` after reviewing."])

    with output_path.open("a", encoding="utf-8") as output:
        output.write("has_due=true\n")
        output.write("issue_title=LeetCode review reminder\n")
        output.write("issue_body<<EOF\n")
        output.write("\n".join(body))
        output.write("\nEOF\n")
    print(f"{len(due)} review(s) due.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage LeetCode spaced repetition reviews.")
    subparsers = parser.add_subparsers(required=True)

    add = subparsers.add_parser("add", help="Add or update a problem in the review schedule.")
    add.add_argument("problem_id", type=int)
    add.add_argument("title")
    add.add_argument("--difficulty", default="Medium", choices=["Easy", "Medium", "Hard"])
    add.add_argument("--topic", default="General")
    add.add_argument("--path", default="")
    add.set_defaults(func=command_add)

    due = subparsers.add_parser("due", help="Show problems due for review.")
    due.add_argument("--date", help="Check due reviews by YYYY-MM-DD. Defaults to today.")
    due.set_defaults(func=command_due)

    review = subparsers.add_parser("review", help="Mark a problem as reviewed.")
    review.add_argument("problem_id", type=int)
    review.add_argument("--result", required=True, choices=["again", "hard", "good", "easy"])
    review.set_defaults(func=command_review)

    github_output = subparsers.add_parser("github-output", help="Write GitHub Actions output for due reviews.")
    github_output.add_argument("--output", required=True)
    github_output.set_defaults(func=command_github_output)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
