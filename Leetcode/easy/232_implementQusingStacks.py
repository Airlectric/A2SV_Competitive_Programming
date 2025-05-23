class MyQueue:

    def __init__(self):
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            return self.items.pop(0)
        

    def peek(self) -> int:
        if not self.empty():
            return self.items[0]


    def empty(self) -> bool:
        if len(self.items) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
