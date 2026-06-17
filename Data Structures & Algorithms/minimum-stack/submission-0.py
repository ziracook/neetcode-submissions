class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] # Stack of min values for each valued added to the stack
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        curmin = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(curmin)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
