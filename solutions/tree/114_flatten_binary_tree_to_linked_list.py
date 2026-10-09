"""
LeetCode: 114. Flatten Binary Tree to Linked List
Approach: tree (Morris-style: splice left subtree in front of right)
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Time: O(n)
Space: O(1)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                # rightmost node of the left subtree is the preorder predecessor
                # of cur.right
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right


# Notes:
# - Intuition: in preorder, the right subtree comes right after the last node of the
#   left subtree. So attach cur.right to the rightmost node of cur.left, then move
#   the left subtree to the right.
# - Edge cases: empty tree, no left children at all.
# - Mistakes: forgetting to set cur.left = None; the result must be a right-only list.
