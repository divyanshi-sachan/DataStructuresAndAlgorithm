class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxarea = 0
        while left<right:
            width = right - left
            curr_height = min(height[left],height[right])
            area = width*curr_height
            maxarea = max(area,maxarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        