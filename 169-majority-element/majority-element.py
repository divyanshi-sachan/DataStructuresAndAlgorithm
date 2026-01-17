class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        for key,value in dict1.items():
            if value > (n//2):
                return key 
            

            