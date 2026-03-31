class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        counter = 0
        for h in range(0, len(height),1):
            if h == 0:
                maxLeft.append(0)
            else:
                maxLeft.append(max(height[:h]))
        for d in range(len(height), 0, -1):
            if d > len(height) -1:
                maxRight.append(0)
            elif d == len(height) -1:
                maxRight.append(height[d])
            else:
                maxRight.append(max(height[d::]))
        maxRight.reverse()
        for k in maxLeft:
            print("MaxLeft",k)
        for b in maxRight:
            print("MaxRight",b)
        for a in range(0, len(height) -1, 1):
            val = min(maxLeft[a],maxRight[a]) - height[a] 
            if min(maxLeft[a],maxRight[a]) - height[a] < 0:
                val = 0
            counter = counter + val
        return counter
        # counter = 0
        # left = -1
        # right = len(height) - 1
        # index = 0
        # array = []
        # while right >= 0:
        #     if left <= 0:
        #         first = 0
        #     else:
        #         first = max(height[:left])
        #     if right == 0:
        #         second = 0
        #     else:
        #         second = max(height[:right])
            

        #     answer = min(first,second) - height[index]
    
        #     if height[right] == 0 and height[left] != 0:
        #         answer = height[left] - height[index]
        
        #     elif answer < 0:
        #         answer = 0
        #     print(first,second)
     
        #     array.append(answer)
            
        #     # if answer < 0:
        #     #     answer = 0
        #     # print(index, height[index], min(height[left],height[right]) )
        #     # print(answer)
        #     # counter = counter + answer
        #     index = index + 1
        #     left = left + 1
        #     right = right - 1
        # for n in array:
        #     counter = counter + n
        # return counter
        
