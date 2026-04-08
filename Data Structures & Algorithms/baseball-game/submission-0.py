class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif operations[i] == "D":
                print("reached")
                stack.append(int(stack[-1])*2)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))
        counter = 0
        for num in stack:
            print(num)
            counter = counter + int(num)
        return counter
        