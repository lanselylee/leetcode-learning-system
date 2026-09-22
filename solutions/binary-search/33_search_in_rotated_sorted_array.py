"""
LeetCode: 33. Search in Rotated Sorted Array
Approach: binary-search
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Time: O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1


# Notes:
# - Intuition: at least one half of any rotated-sorted range is normally ordered;
#   determine which half is sorted, then check if target lies in that range.
# - Edge cases: empty array, no rotation, target not present, single element.
# - Mistakes: using strict < instead of <= when checking nums[lo] <= nums[mid].
