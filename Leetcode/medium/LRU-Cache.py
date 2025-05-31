class ListNode:
    def __init__(self,key=0,val=0):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head,self.tail = ListNode(),ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def _remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev
    
    def add_to_front(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self.add_to_front(node)
        return node.val

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self.add_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                print(lru.key)
                del self.cache[lru.key]

            node = ListNode(key,value)
            self.add_to_front(node)
            self.cache[key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)