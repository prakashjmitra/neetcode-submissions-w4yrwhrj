class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        counter = 0
        for i in tokens:
            if i == "+":
                counter = int(stack[-1]) + int(stack[-2])
                print(stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print("addition",counter)
            elif i == "-":
                counter = int(stack[-2]) - int(stack[-1])
                print(stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print("sub",counter)
            elif i == "*":
                counter = int(stack[-1]) * int(stack[-2])
                print(stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print("m",counter)
            elif i == "/":
                counter = int(int(stack[-2])/int(stack[-1]))
                print(stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print("d",counter)
            else:
                stack.append(i)
        return int(stack[-1])



        