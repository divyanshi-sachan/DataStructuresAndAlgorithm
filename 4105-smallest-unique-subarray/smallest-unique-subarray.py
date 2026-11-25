
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base = 911382323
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        for i in range(n):
            h1[i + 1] = (h1[i] * base + nums[i]) % mod1
            h2[i + 1] = (h2[i] * base + nums[i]) % mod2
            p1[i + 1] = (p1[i] * base) % mod1
            p2[i + 1] = (p2[i] * base) % mod2
        def check(k):
            freq = {}
            for i in range(n - k + 1):
                j = i + k
                x = (h1[j] - h1[i] * p1[k]) % mod1
                y = (h2[j] - h2[i] * p2[k]) % mod2
                key = (x, y)
                freq[key] = freq.get(key, 0) + 1
                if freq[key] == 2:
                    pass
            return any(v == 1 for v in freq.values())
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
