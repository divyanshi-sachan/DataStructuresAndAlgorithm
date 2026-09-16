class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        def func(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            take = nums[i] + func(i+2)
            not_take = func(i+1)
            memo[i] = max(take,not_take)
            return memo[i]
        return func(0)

        