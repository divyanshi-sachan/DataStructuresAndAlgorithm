class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def func(i):
            if i == n:
                return 1
            if i>n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = func(i+1)+func(i+2)
            return memo[i]
        return func(0)



        