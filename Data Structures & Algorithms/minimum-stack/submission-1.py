class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = 0
        self.min_stack = []

    def push(self, val: int) -> None:
    
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        print(self.min_stack[-1])
        return self.min_stack[-1]
        
