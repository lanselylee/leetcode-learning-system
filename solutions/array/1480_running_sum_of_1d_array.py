"""
LeetCode: 1480. Running Sum of 1d Array
Approach: array
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Time: O(n)
Space: O(1) extra (excluding output array)
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


# Notes:
# - Intuition: runningSum[i] = runningSum[i-1] + nums[i], so accumulate in place.
# - Edge cases: empty array, single element array.
# - Mistakes: none.
