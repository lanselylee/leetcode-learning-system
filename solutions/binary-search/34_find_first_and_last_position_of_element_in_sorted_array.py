"""
LeetCode: 34. Find First and Last Position of Element in Sorted Array
Approach: binary-search
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Time: O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_left: bool) -> int:
            lo, hi = 0, len(nums) - 1
            result = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    result = mid
                    if is_left:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return result

        return [find_bound(True), find_bound(False)]


# Notes:
# - Intuition: run binary search twice, one biased to keep shrinking left on a match
#   (finds leftmost index), one biased to keep shrinking right (finds rightmost index).
# - Edge cases: empty array, target not present, target appears once, all elements equal target.
# - Mistakes: forgetting to keep searching (not returning immediately) after finding a match.
