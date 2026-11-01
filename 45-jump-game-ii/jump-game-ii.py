class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0
        n = len(nums)
        for i in range(n-1):
            farthest = max(farthest,i+nums[i])
            if i == curr_end:
                jumps+=1
                curr_end = farthest
        return jumps
        