class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for n in range(0, len(position),1):
            combined.append([position[n],speed[n]])
        combined.sort(reverse = True)
        stack = []
        for n in range(0, len(combined),1):
            time = (target - combined[n][0])/combined[n][1]
            if len(stack) >= 1 and time <= stack[-1]:
                pass
            else:
                stack.append(time)
        return len(stack)
            
        