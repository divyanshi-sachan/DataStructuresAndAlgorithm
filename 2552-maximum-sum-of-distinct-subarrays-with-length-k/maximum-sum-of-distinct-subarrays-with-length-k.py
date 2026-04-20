class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        windowSum = sum(nums[:k])
        maxSum = 0
        freq = {}
        n  = len(nums)
        for ch in nums[:k]:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch] = 1
        if len(freq) == k:
            maxSum = max(windowSum,maxSum)
        for i in range(k,n):
            out = nums[i-k]
            if freq[out] == 1:
                del freq[out]
            else:
                freq[out]-=1
            windowSum -=nums[i-k]
            ins = nums[i]
            if ins in freq:
                freq[ins]+=1
            else:
                freq[ins] = 1
            windowSum+=nums[i]
            if len(freq) == k:
                maxSum = max(maxSum, windowSum)
        return maxSum
            



        