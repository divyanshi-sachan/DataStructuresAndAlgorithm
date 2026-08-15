class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in dict1:
                return [dict1[complement],i]
            dict1[num] = i


        