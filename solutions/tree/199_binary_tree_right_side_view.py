"""
LeetCode: 199. Binary Tree Right Side View
Approach: tree (BFS level order)
Link: https://leetcode.com/problems/binary-tree-right-side-view/
Time: O(n)
Space: O(w), w = max width of the tree
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                # push right child first so the first node of each level is the rightmost
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res


# Notes:
# - Intuition: the right side view is the last node of each level; BFS level by level
#   (enqueue right before left so it's the first one popped).
# - Edge cases: empty tree; a left-only branch deeper than the right one is still visible.
# - Mistakes: only walking the right spine misses deeper left nodes.
