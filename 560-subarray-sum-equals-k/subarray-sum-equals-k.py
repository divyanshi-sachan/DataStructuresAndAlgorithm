class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        dict1 = {0:1}
        count = 0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in dict1:
                count+=dict1[prefix_sum-k]
            if prefix_sum in dict1:
                dict1[prefix_sum] += 1
            else:
                dict1[prefix_sum] = 1
        return count
            

        