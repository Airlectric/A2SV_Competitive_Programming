# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before_rev = ListNode()
        after_rev = ListNode()

        before = before_rev
        after = after_rev
        new_head = None
        next_ = None

        current = head
        count = 1

        while current and count <= right:
            if count < left:
                before.next = current
                before = before.next
                print('bef', before)
                current = current.next
            elif count >= left and count <= right:
                next_ = current.next
                current.next = new_head
                new_head = current
                current = next_
                print(new_head)
            count += 1
        
        
        curr = new_head
        while curr.next:
            curr = curr.next
        
        curr.next = next_
        
        before.next = new_head

        return before_rev.next
                    


        