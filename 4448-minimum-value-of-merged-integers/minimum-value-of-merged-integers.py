class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b =float('inf')
        for i in range(0, len(nums), 2):
            m = int(str(nums[i]) + str(nums[i+1]))
            b = min(b, m)
        return b