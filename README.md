# LeetCode Learning & Review System

![LeetCode Stats](https://leetcard.jacoblin.cool/xiaomeng)

This repository is not just a collection of accepted solutions.

It is my algorithm learning system for Python problem solving, pattern-based practice, failure analysis, and spaced repetition review.

My goal is to become a stronger problem-solving engineer by tracking how I think, where I get stuck, and when I should revisit a problem.

## What This Repository Contains

### 1. LeetCode Solutions

Accepted submissions and manually polished notes are organized by problem or topic.

```text
leetcode/
├── easy/
├── medium/
└── hard/
```

### 2. Failure Logs

This is the most valuable part of the system.

When I struggle with a problem, I record:

- what I tried first
- why it failed
- which mental model was wrong
- what pattern I learned

```text
failure_logs/
├── dp/
├── greedy/
├── intervals/
└── backtracking/
```

### 3. Spaced Repetition Review

Each important problem can be added to a memory-curve schedule. The review queue tells me what to revisit next.

```bash
python3 scripts/review.py due
```

GitHub Actions checks the queue every morning and can create a reminder issue when problems are due.

## Review Workflow

Add a newly solved problem:

```bash
python3 scripts/review.py add 39 "Combination Sum" --difficulty Medium --topic Backtracking --path backtracking/39_combination_sum.py
```

See what is due today:

```bash
python3 scripts/review.py due
```

Mark a review result:

```bash
python3 scripts/review.py review 39 --result good
```

Review results use a simple memory curve:

| Result | Meaning | Next Review |
| --- | --- | --- |
| `again` | I forgot the idea or could not solve it | tomorrow |
| `hard` | I solved it, but it was slow or shaky | in 3 days |
| `good` | I solved it with minor friction | interval grows |
| `easy` | I solved it confidently | interval grows faster |

## Current Focus

- Backtracking patterns
- Dynamic programming state design
- Greedy vs. DP boundary cases
- Binary search and two-pointer templates
- Interview-ready Python implementations

## Featured Notes

| Problem | Topic | File |
| --- | --- | --- |
| 1. Two Sum | Hash Map | [1_two_sum.py](1_two_sum.py) |
| 39. Combination Sum | Backtracking | [backtracking/39_combination_sum.py](backtracking/39_combination_sum.py) |
| 189. Rotate Array | Array / Two Pointers | [189_rotate_array.py](189_rotate_array.py) |

## Repository Structure

```text
.
├── .github/workflows/
│   ├── leetcode-stats.yml
│   └── review-reminder.yml
├── data/
│   └── review_schedule.json
├── scripts/
│   └── review.py
├── templates/
│   └── general_template.py
├── problems.md
└── topic folders and solution files
```

## Tech

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat&logo=leetcode&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)

## Links

- LeetCode problem list: [进击的小狗](https://leetcode.com/problem-list/2u418x6r/)
- GitHub profile: [@lanselylee](https://github.com/lanselylee)
