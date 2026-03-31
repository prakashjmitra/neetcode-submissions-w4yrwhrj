class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min > val:
            self.min = val

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
