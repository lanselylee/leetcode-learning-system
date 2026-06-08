"""
LeetCode ✏️: 39. Combination Sum
Approach 📒: Backtracking + DFS
Link 🔗: https://leetcode.com/problems/combination-sum/
Time ⏱️: O(2^n)
Space 💾: O(n)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(start, path, remain):
            if remain == 0:  # if the remaining target is 0, add the path to the result
                res.append(path[:])  # deep copy the path
                return
            
            if remain < 0:  # if the remaining target is less than 0, return
                return

            for i in range(start, len(candidates)):  # iterate through the candidates
                path.append(candidates[i])
                dfs(i, path, remain - candidates[i])  # dfs with the new start index and the new remaining target
                path.pop()  # pop the last element of the path
        
        dfs(0, [], target)  # start the dfs with the first index and the target as the remaining target    
        return res

# Notes:
# 1. Use DFS to find all the combinations that sum to target
# 2. Use a start index to avoid duplicate combinations
# 3. Use remain to track the remaining target
# 4. Use path to store the current combination
# 5. Use res to store all the combinations
# 6. Backtrack by popping the last element after each recursive call
