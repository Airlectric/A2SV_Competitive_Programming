from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.target = []
        self.queue = deque()
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.target.append(1)
        
        if len(self.queue) > self.k:
            popped = self.queue.popleft()
            if popped == self.value:
                self.target.pop()

        return len(self.target) == self.k
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)