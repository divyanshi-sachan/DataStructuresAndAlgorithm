class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        window_sum = 0
        min_length = float('inf')
        for right in range(n):
            window_sum += nums[right]
            while window_sum>=target:
                curr_len =right - left + 1
                min_length = min(min_length,curr_len)
                window_sum -=nums[left]
                left += 1
        if min_length == float('inf'):
            return 0 
        else:
            return min_length

        



        
        