class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1 = {}
        for i,val in enumerate(nums):
            complement = target-val
            if complement in dict1:
                return [dict1[complement],i]
            dict1[val]=i
        return -1

        