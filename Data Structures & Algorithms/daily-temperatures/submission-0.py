class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for n in range(0, len(temperatures),1):
            maximum = temperatures[n]
            pos = 0
            for k in range(0, len(temperatures),1):
                if temperatures[k] > maximum and k > n:
                    pos = k - n 
                    break
            result.append(pos)
        return result
                

        