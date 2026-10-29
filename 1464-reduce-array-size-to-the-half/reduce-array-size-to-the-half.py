class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        n = len(arr)
        count = 0
        dict1 = {}
        for ele in arr:
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele] = 1
        dict1 = sorted(dict1.values(),reverse = True)
        remaining = len(arr)
        count = 0
        for value in dict1:
            remaining-=value
            count+=1
            if remaining<=n//2:
                return count


        
        