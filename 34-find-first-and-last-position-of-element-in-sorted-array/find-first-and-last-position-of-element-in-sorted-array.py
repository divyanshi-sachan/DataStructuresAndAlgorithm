class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums, target), self.last(nums, target)]
    def first(self,nums,target):
        ans= -1
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if target>nums[mid]:
                start = mid+1
            elif target<nums[mid]:
                end = mid-1
            else:
                ans=mid
                end=mid-1
        return ans
    def last(self,nums,target):
        ans= -1
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if target>nums[mid]:
                start = mid+1
            elif target<nums[mid]:
                end = mid-1
            else:
                ans=mid
                start=mid+1
        return ans
        