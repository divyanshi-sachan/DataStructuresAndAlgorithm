class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 and nums[0] == 1:
            print("!!!")
            return 2
        exist = set()
        for i in range(1,n+1):
            exist.add(i)
        print(exist)
        for i in range(n):
            if nums[i] in exist:
                exist.remove(nums[i])
        if not exist:
            return n+1
        return min(exist)


    

        