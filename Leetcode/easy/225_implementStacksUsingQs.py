class MyStack:

    def __init__(self):
        self.items = []

    
    def push(self, x: int) -> None:
        self.items.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            return self.items.pop()
        else:
            print('stack is empty')
        

    def top(self) -> int:
        if not self.empty():
            return self.items[-1]
        

    def empty(self) -> bool:
        if len(self.items) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
