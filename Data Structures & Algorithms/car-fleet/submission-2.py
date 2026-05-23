class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for n in range(len(position)):
            combined.append([position[n], speed[n]])
        combined.sort(key = lambda x: x[0])
        combined.reverse()
        stack = []
        for k in combined:
            print(k)
        for i in range(len(combined)):
            time = (target - combined[i][0])/combined[i][1]
            if not stack:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)

            

            
        