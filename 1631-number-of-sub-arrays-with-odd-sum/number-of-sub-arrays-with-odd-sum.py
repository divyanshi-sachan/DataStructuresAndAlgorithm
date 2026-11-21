class Solution:
    def numOfSubarrays(self,arr:list[int])->int:
        mod=10**9+7
        odd=0
        even=1
        ans=0
        parity=0
        for x in arr:
            parity^=x%2
            if parity:
                ans+=even
                odd+=1
            else:
                ans+=odd
                even+=1
        return ans%mod