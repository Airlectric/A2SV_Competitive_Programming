class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        node = self.head
        while node and count != index:
            node = node.next
            count += 1
        return node.val if node != None else -1


    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        node = ListNode(val)
        current = self.head
        count = 0
        while current and count != index-1:
            current = current.next
            count += 1

        if current:
            node.next = current.next
            current.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        count = 0
        while count != index-1 and current != None:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next
    
    def displayList(self):
        curr = self.head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        print(arr)





# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)