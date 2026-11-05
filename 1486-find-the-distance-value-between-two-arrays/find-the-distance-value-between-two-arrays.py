class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for num in arr1:
            found = False
            for x in arr2:
                if abs(num - x) <= d:
                    found = True
                    break
            if not found:
                count += 1
        return count