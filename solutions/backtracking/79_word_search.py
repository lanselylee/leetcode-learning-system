"""
LeetCode: 79. Word Search
Approach: Backtracking + DFS on grid
Link: https://leetcode.com/problems/word-search/
Time: O(m * n * 4^L) where L is len(word)
Space: O(L) recursion stack
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):  # all index
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1) or
                     dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
