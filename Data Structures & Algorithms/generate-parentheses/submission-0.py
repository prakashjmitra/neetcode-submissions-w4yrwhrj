class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def generateHelper(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                generateHelper(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                generateHelper(openN, closedN + 1)
                stack.pop()
        
        generateHelper(0,0)
        return res