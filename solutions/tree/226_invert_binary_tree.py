"""
LeetCode: 226. Invert Binary Tree
Approach: tree (recursive DFS)
Link: https://leetcode.com/problems/invert-binary-tree/
Time: O(n)
Space: O(h) recursion stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# Notes:
# - Intuition: swap left and right children at every node, recursively.
# - Edge cases: empty tree, single node.
# - Mistakes: swapping sequentially (root.left = invert(root.right) then
#   root.right = invert(root.left)) uses the already-overwritten left; swap in one tuple assignment.
