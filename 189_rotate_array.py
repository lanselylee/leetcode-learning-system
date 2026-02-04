from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        
        if n == 0:
            return 
        k %= n
        
        def reverse(l :int, r: int) -> None:
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1
        reverse(0,n-1)
        reverse(0, k - 1)
        reverse(k, n-1)