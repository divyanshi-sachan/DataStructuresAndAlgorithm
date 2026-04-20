class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = set()
        left = 0
        sum1=0
        max_sum = 0
        n = len(nums)
        for right in range(n):
            while nums[right] in freq:
                freq.remove(nums[left])
                sum1-=nums[left]
                left+=1
            freq.add(nums[right])
            sum1+=nums[right]
            max_sum = max(sum1,max_sum)
        return max_sum



        