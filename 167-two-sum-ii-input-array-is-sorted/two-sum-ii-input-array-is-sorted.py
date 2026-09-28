class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict1 = {}
        for i,num in enumerate(numbers):
            if target-num in dict1:
                return [dict1[target-num],i+1]
            dict1[num] = i+1
        return -1
            
        