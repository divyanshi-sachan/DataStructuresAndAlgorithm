class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        freq = {0:1}
        prefix = 0
        for x in nums:
            prefix+=x
            if prefix-k in freq:
                count+=freq[prefix-k]
            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix] = 1
        return count

