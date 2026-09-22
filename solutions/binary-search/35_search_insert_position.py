"""
LeetCode: 35. Search Insert Position
Approach: binary-search
Link: https://leetcode.com/problems/search-insert-position/
Time: O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo


# Notes:
# - Intuition: standard lower-bound binary search; lo ends up at the first index
#   whose value is >= target, which is exactly where target should be inserted.
# - Edge cases: target smaller than all elements, larger than all elements, empty array.
# - Mistakes: using an inclusive hi = len(nums) - 1 and mishandling the insert-at-end case.
