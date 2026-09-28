class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0]*n
        prefix = [0]*n
        suffix = [0]*n
        prefix[0]= nums[0]
        suffix[-1] = nums[-1]
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i]
        for i in range(n):
            if i == 0:
                left = 1
            else:
                left = prefix[i-1]
            if i== n-1:
                right = 1
            else:
                right = suffix[i+1]
            answer[i] = left*right
        return answer



        