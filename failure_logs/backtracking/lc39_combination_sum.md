# 39. Combination Sum

## Original Mistake

The tempting first approach is to treat this like a normal subset problem and always move to the next index after choosing a number. That misses valid answers because each candidate can be reused.

Another common mistake is restarting the loop from `0` in every recursive call. That creates duplicate combinations such as `[2, 2, 3]` and `[2, 3, 2]`.

## Correct Mental Model

This is a combination search, not a permutation search.

The `start` index controls which candidates are allowed from the current point onward:

- use `dfs(index, ...)` when the same number can be reused
- use `dfs(index + 1, ...)` when each number can be used once

For this problem, `dfs(index, path, remain - candidates[index])` is the key line because choosing `candidates[index]` does not remove it from future choices.

## Pattern Learned

Backtracking problems often differ by one small decision:

| Problem Type | Recursive Step |
| --- | --- |
| Combination, reusable choices | `dfs(index, ...)` |
| Combination, single-use choices | `dfs(index + 1, ...)` |
| Permutation | track `used` instead of `start` |

## Review Checklist

- Can I explain why `start` prevents duplicate combinations?
- Can I explain why this problem uses `dfs(index, ...)` instead of `dfs(index + 1, ...)`?
- Can I rewrite the solution without looking?
