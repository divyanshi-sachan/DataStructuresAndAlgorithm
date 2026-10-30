class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        def findFirstOccurence(nums):
            left = 0
            right = n-1
            ans = -1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]<target:
                    left = mid+1
                elif nums[mid]>target:
                    right = mid-1
                else:
                    ans = mid
                    right = mid-1
            return ans
        def findLastOccurence(nums):
            ans = -1
            left = 0
            right = n-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]<target:
                    left = mid+1
                elif nums[mid]>target:
                    right = mid-1
                else:
                    ans = mid
                    left = mid+1
            return ans
        first = findFirstOccurence(nums)
        last = findLastOccurence(nums)
        return [first,last]


        