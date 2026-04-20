class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        k=3
        freq = {}
        n = len(s)
        window = s[:k]
        for ch in window:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        if len(freq) == k:
            count+=1
        for i in range(k,n):
            out = i-k
            if s[out] in freq:
                if freq[s[out]] ==1:
                    del freq[s[out]]
                else:
                    freq[s[out]]-=1
            ins = i
            if s[ins] in freq:
                freq[s[ins]]+=1
            else:
                freq[s[ins]]=1
            if len(freq) == k:
                count+=1
        return count 
                         

        
        