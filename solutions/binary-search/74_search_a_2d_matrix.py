"""
LeetCode: 74. Search a 2D Matrix
Approach: binary-search
Link: https://leetcode.com/problems/search-a-2d-matrix/
Time: O(log(m * n))
Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False


# Notes:
# - Intuition: treat the matrix as one flattened sorted array since each row's
#   first element is greater than the previous row's last; map a 1D index to (row, col).
# - Edge cases: empty matrix, single row/column, target smaller/larger than all values.
# - Mistakes: using integer division/mod with the wrong dimension (cols vs rows).
