class Solution:
    def findSubtreeSizes(self,parent:List[int],s:str)->List[int]:
        n=len(parent)
        children=[[] for _ in range(n)]
        for i in range(1,n):
            children[parent[i]].append(i)
        nearest=[-1]*26
        new_parent=parent[:]
        def dfs(node):
            ch=ord(s[node])-ord('a')
            if nearest[ch]!=-1:
                new_parent[node]=nearest[ch]
            old=nearest[ch]
            nearest[ch]=node
            for child in children[node]:
                dfs(child)
            nearest[ch]=old
        dfs(0)
        new_children=[[] for _ in range(n)]
        for i in range(1,n):
            new_children[new_parent[i]].append(i)
        ans=[1]*n
        def calc(node):
            for child in new_children[node]:
                calc(child)
                ans[node]+=ans[child]
        calc(0)
        return ans