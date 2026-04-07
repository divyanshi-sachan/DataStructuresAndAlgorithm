class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[end]!=nums[end-1]:
            return nums[end]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or \
                (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                start = mid + 1
            else:
                end = mid - 1
        