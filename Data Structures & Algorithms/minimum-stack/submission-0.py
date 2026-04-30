class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        current_min=val
        if self.min_stack:
            current_min=min(current_min, self.min_stack[-1] )
        else:
            self.min_stack.append(current_min)
        self.min_stack.append(current_min)


    def pop(self) -> None:
        if not self.stack and not self.min_stack:
            return None
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]