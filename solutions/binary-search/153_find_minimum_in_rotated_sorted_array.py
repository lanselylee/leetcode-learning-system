"""
LeetCode: 153. Find Minimum in Rotated Sorted Array
Approach: binary-search
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Time: O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]


# Notes:
# - Intuition: compare the middle element to the rightmost element; if mid is greater,
#   the minimum must be to the right of mid, otherwise it's at mid or to its left.
# - Edge cases: no rotation (already sorted), single element, two elements.
# - Mistakes: comparing nums[mid] to nums[lo] instead of nums[hi], which breaks
#   when the left half itself is not sorted relative to mid.
