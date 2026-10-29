class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        n = len(capacity)
        remaining = []
        for i in range(n):
            remaining.append(capacity[i]-rocks[i])
        remaining.sort()
        count = 0
        for ele in remaining:
            if additionalRocks>=ele:
                additionalRocks-=ele
                count+=1
        return count





        