class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        k = self.stack.pop()
        print(f"Pop elemtn is : {k}")

    def top(self) -> int:
        length = len(self.stack)
        return self.stack[length - 1]

    def getMin(self) -> int:
        min = self.stack[0]
        for i in self.stack:
            if i < min:
                min = i
        return min
        
