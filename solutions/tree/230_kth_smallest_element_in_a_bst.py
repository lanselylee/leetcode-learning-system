"""
LeetCode: 230. Kth Smallest Element in a BST
Approach: tree (iterative inorder traversal)
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Time: O(h + k)
Space: O(h) stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return -1


# Notes:
# - Intuition: inorder traversal of a BST visits values in sorted order, so the k-th
#   popped node is the answer; iterative lets us stop early.
# - Edge cases: k = 1 (leftmost node), k = n (rightmost node).
# - Mistakes: forgetting to move to cur.right after visiting a node.
