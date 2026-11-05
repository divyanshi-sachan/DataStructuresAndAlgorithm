class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = 0
        n = len(nums)
        curr_sum = 0
        max_sum = 0
        seen = set()
        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum-=nums[left]
                left+=1
            seen.add(nums[right])
            curr_sum+=nums[right]
            max_sum = max(curr_sum,max_sum)
        return max_sum

        