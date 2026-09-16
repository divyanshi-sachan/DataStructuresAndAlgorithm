class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        max_len = 0
        n = len(nums)
        freq = {0:-1}
        for i  in  range(n):
            if nums[i] == 0:
                prefix-=1
            else:
                prefix+=1
            if prefix in freq:
                max_len = max(max_len,i-freq[prefix])
            else:
                freq[prefix] = i
        return max_len



        