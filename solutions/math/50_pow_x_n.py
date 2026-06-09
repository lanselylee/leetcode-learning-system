"""
LeetCode: 50. Pow(x,n)
Approach: Math
Link: https://leetcode.com/problems/powx-n/
Time: O(log n)
Space: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        exponent = abs(n)
        result = 1.0
        base = x

        while exponent:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return result if n >= 0 else 1 / result


# Notes:
# - Intuition: Use binary exponentiation instead of multiplying x n times.
# - Edge cases: Negative n means invert the final result.
# - Mistakes: Remember to square the base each round and halve the exponent.
