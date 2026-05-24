class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele = None

    def push(self, val: int) -> None:
        if self.min_ele == None: 
            self.min_ele = val
        else:
            self.min_ele = min(self.min_ele, val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        if self.stack:
            self.min_ele = min(self.stack)
        else:
            self.min_ele = None

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_ele
