class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0 
        right = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                height = min(heights[i],heights[j]) * (abs(j - i))
                maximum = max(height, maximum)
        return maximum

            
            


        