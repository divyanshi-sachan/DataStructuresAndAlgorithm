class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        length = len(nums)
        n=length//2
        dict1={}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num]+=1
                return num
        return -1