class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        counter = 0
        for n in tokens:
            if n == "+" and len(stack)>=2:
                print(stack[-1],stack[-2])
                counter = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print(counter, "add")
            
            elif n == "-" and len(stack)>=2:
                print(stack[-1],stack[-2])
                counter = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print(counter, "subtract")

            elif n == "*" and len(stack)>=2:
                print(stack[-1],stack[-2])
                counter = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(counter)
                print(counter,"multiply")
            elif n == "/" and len(stack)>=2:
                print(stack[-1],stack[-2])
                counter = int(int(stack[-2])/int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(counter)
                print(counter, "divide")
            else:
                stack.append(n)
        if len(tokens) ==1:
            return int(tokens[0])
        return counter

        