"""
LeetCode: 70. Climbing Stairs
Approach: DP
Link: https://leetcode.com/problems/climbing-stairs/
Time: O(n)
Space: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_two = 1
        prev_one = 2

        for _ in range(3, n + 1):
            current = prev_one + prev_two
            prev_two = prev_one
            prev_one = current

        return prev_one


# Notes:
# - Intuition: To reach step i, you can come from i - 1 or i - 2.
# - Edge cases: n = 1 returns 1, n = 2 returns 2.
# - Mistakes: Do not allocate a full DP array when only the previous two states are needed.
