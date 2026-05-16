class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif character == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif character == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return len(stack) == 0
            
        