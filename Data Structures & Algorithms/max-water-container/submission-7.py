class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0 
        right = len(heights) - 1
        for i in range(len(heights)):
            while left < right:
                height = min(heights[left], heights[right]) * (right - left)
                maximum = max(maximum, height)
                if heights[left] < heights[right]:
                    left = left + 1
                else:
                    right = right - 1
        return maximum

            
            


        