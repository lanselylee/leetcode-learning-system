"""
LeetCode: 124. Binary Tree Maximum Path Sum
Approach: tree (post-order DFS)
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Time: O(n)
Space: O(h) recursion stack, h = tree height
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            best = max(best, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return int(best)


# Notes:
# - Intuition: for each node, the best "path through this node" combines its value
#   with the best non-negative gain from each child; track that globally while the
#   return value (usable by the parent) can only extend through one child.
# - Edge cases: single node, all negative values, only left/right children present.
# - Mistakes: returning the two-branch sum to the caller instead of the single-branch
#   gain, which would let the parent "use" both children, violating the path definition.
