class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                maximum = max(min(heights[i], heights[j]) * abs(j-i), maximum)
        return maximum
            
            


        