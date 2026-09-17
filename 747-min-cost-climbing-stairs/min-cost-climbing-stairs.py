class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = {}
        def func(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(func(i+1),func(i+2))
            return memo[i]
        return min(func(0),func(1))
        
        