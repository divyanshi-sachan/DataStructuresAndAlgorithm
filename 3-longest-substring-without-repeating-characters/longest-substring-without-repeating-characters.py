class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        dict1 = {}
        for right in range(len(s)):
            char = s[right]
            while char in dict1:
                del dict1[s[left]]
                left+=1
            dict1[char] = 1
            curr_len = right-left+1
            max_len = max(curr_len,max_len)
        return max_len

                


            



        