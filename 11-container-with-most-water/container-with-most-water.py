class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        maxArea = 0
        right = n-1
        while left<right:
            width = right-left
            h = min(height[left],height[right])
            area = width*h
            maxArea = max(maxArea,area)
            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return maxArea

        