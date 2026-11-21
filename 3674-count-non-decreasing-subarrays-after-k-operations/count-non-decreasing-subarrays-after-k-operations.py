class Solution:
    def countNonDecreasingSubarrays(self,nums:List[int],k:int)->int:
        n=len(nums)
        nxt=[n]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if st:
                nxt[i]=st[-1]
            st.append(i)
        m=n.bit_length()
        up=[nxt]+[[n]*n for _ in range(m-1)]
        w=[[nums[i]*(nxt[i]-i) for i in range(n)]]
        for j in range(1,m):
            p=up[j-1]
            up[j]=[p[p[i]] if p[i]<n else n for i in range(n)]
            w.append([w[j-1][i]+(w[j-1][p[i]] if p[i]<n else 0) for i in range(n)])
        pref=[0]
        for x in nums:
            pref.append(pref[-1]+x)
        def cost(l,r):
            cur=l
            total=0
            for j in range(m-1,-1,-1):
                nxt_pos=up[j][cur]
                if nxt_pos<=r:
                    total+=w[j][cur]
                    cur=nxt_pos
            total+=nums[cur]*(r-cur+1)
            return total-(pref[r+1]-pref[l])
        ans=0
        l=0
        for r in range(n):
            while l<=r and cost(l,r)>k:
                l+=1
            ans+=r-l+1
        return ans