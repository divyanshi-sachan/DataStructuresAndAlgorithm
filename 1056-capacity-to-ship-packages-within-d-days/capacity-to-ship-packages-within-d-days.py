class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            day_used = 1
            current_load = 0
            for weight in weights:
                if current_load+weight<=capacity:
                    current_load+=weight
                else:
                    day_used+=1
                    current_load=weight
            return day_used<=days
        left,right = max(weights),sum(weights)
        while left<=right:
            mid = (left+right)//2
            if possible(mid):
                right = mid-1
            else:
                left=mid+1
        return left        