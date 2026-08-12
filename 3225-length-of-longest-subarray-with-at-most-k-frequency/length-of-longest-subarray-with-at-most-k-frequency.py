class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        freq = {}
        max_len = 0
        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]] = 1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            max_len = max(max_len,right-left+1)
        return max_len




        