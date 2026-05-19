class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            reached = False
            for j in range(len(temperatures)):
                if (temperatures[j] > temperatures[i]) and j > i:
                    reached = True
                    result.append(j-i)
                    break
            if not reached:
                result.append(0)
        return result
             
           

                

        