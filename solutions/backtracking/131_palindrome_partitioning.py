"""
LeetCode: 131. Palindrome Partitioning
Approach: Backtracking + palindrome check
Link: https://leetcode.com/problems/palindrome-partitioning/
Time: O(n * 2^n)
Space: O(n)
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_pal(start, end):
            l = start
            r = end

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                if is_pal(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res
