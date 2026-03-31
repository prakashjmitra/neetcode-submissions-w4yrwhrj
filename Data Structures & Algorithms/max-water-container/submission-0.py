class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights)):
            for k in range(len(heights)):
                if i != k:
                    if min(heights[i],heights[k]) * abs((k-i)) > maximum:
                        print(min(heights[i],heights[k]), abs(k-i))
                        maximum = min(heights[i],heights[k]) * abs((k-i))
        return maximum

        