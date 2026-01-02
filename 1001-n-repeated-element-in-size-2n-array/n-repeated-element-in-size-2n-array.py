class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        length = len(nums)
        n=length//2
        dict1={}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]]+=1
        for i,value in dict1.items():
            if value == n:
                return i
        return -1