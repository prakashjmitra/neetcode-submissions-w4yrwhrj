class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character == "(" or character == "{" or character == "[":
                stack.append(character)
            if character == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if character == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            if character == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
        