"""
LeetCode: 105. Construct Binary Tree from Preorder and Inorder Traversal
Approach: tree (recursion + hash map of inorder indices)
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Time: O(n)
Space: O(n) for the index map + O(h) recursion stack
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        pre_i = 0

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal pre_i
            if lo > hi:
                return None

            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)

            mid = idx[root_val]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)


# Notes:
# - Intuition: preorder[0] is the root; its position in inorder splits the left and
#   right subtrees. Consume preorder left-to-right, building left before right.
# - Edge cases: single node, skewed trees (all left / all right).
# - Mistakes: using inorder.index() each call makes it O(n^2); must build the left
#   subtree before the right since preorder is root -> left -> right.
