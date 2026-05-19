class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        # for i in range(len(temperatures)):
        #     reached = False
        #     for j in range(len(temperatures)):
        #         if (temperatures[j] > temperatures[i]) and j > i:
        #             reached = True
        #             result.append(j-i)
        #             break
        #     if not reached:
        #         result.append(0)
        # return result
        result = [0] * len(temperatures)
        stack = []
        stack.append([temperatures[0], 0])
        counter = 0
        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
                
            stack.append([temperatures[i], i])
        return result
                


                


             
           

                

        