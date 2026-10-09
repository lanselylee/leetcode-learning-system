"""
LeetCode: 108. Convert Sorted Array to Binary Search Tree
Approach: tree (divide and conquer)
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Time: O(n)
Space: O(log n) recursion stack
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(nums) - 1)


# Notes:
# - Intuition: picking the middle element as root keeps both halves the same size,
#   so the resulting BST is height-balanced.
# - Edge cases: single element, even length (either middle works).
# - Mistakes: slicing nums[:mid] each call adds O(n log n) copying; pass indices instead.
