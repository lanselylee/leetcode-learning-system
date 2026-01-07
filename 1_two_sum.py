class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_to_nums = {}
        for index , num in enumerate(nums):
            complement = target - num

            if complement in index_to_nums:
                return [index_to_nums[complement],index]
            index_to_nums[num] = index