import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(mid,arr):
            hours=0
            for i in range(len(arr)):
                hours+=math.ceil(arr[i]/mid)
            return hours<=h
        left,right=1,max(piles)
        while left<=right:
            mid = (left+right)//2
            if can_finish(mid,piles):
                right=mid-1
            else:
                left=mid+1
        return left

        