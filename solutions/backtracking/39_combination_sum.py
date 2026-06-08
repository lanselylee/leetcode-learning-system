"""
LeetCode: 39. Combination Sum
Approach: Backtracking + DFS
Link: https://leetcode.com/problems/combination-sum/
Time: O(2^n)
Space: O(n)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(start: int, path: list[int], remain: int) -> None:
            if remain == 0:
                results.append(path[:])
                return
            if remain < 0:
                return

            for index in range(start, len(candidates)):
                path.append(candidates[index])
                dfs(index, path, remain - candidates[index])
                path.pop()

        dfs(0, [], target)
        return results
