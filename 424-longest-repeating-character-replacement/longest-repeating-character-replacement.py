class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        max_freq = 0
        left=0
        dict1={}
        for right in range(n):
            if s[right] in dict1:
                dict1[s[right]]+=1
            else:
                dict1[s[right]] = 1
            max_freq= max(max_freq,dict1[s[right]])
            while right-left+1-max_freq>k:
                dict1[s[left]] -= 1
                left+=1
            max_len = max(max_len, right - left + 1)
        return max_len 
            







        