"""
LeetCode: 4. Median of Two Sorted Arrays
Approach: binary-search
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Time: O(log(min(m, n)))
Space: O(1)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1

        raise ValueError("Input arrays are not sorted")


# Notes:
# - Intuition: binary search on the partition index of the shorter array so that
#   left halves of both arrays combined always hold exactly half the total elements.
# - Edge cases: one array empty, arrays of very different lengths, odd/even total length.
# - Mistakes: forgetting to always binary search on the smaller array (keeps j in bounds).
