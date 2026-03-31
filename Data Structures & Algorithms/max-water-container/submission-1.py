class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximum = 0
        # for i in range(len(heights)):
        #     for k in range(len(heights)):
        #         if i != k:
        #             if min(heights[i],heights[k]) * abs((k-i)) > maximum:
        #                 print(min(heights[i],heights[k]), abs(k-i))
        #                 maximum = min(heights[i],heights[k]) * abs((k-i))
        # return maximum
        left = 0 
        right = 1
        maximum = 0
        while left <= len(heights) -1:
            if right == len(heights) -1:
                right = 0
                left = left + 1
                continue
            if right != left:
                if (min(heights[left],heights[right]) * abs(right - left) > maximum):
                    maximum = min(heights[left],heights[right]) * abs(right - left)
            right = right + 1
        return maximum
            


        