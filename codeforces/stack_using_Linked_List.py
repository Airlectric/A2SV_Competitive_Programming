class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,val):
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.head.next
        return temp.val

    def peek(self):
        if not self.head:
            return -1
        return self.head.val

    def isEmpty(self):
        return not self.head


if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    stack.push(7)
    stack.push(9)
    stack.push(4)
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.isEmpty())
