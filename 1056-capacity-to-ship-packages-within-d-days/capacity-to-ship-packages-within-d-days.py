class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            day = 1
            load = 0
            for weight in weights:
                if load + weight<=capacity:
                    load+=weight
                else:
                    day+=1
                    load = weight
            return day<=days
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid = (left+right)//2
            if possible(mid):
                right = mid-1
            else:
                left = mid+1
        return left

        