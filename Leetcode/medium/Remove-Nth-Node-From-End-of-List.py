# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode()
        dummy.next = head
        toEnd = head
        current = dummy

        while toEnd:
            length += 1
            toEnd = toEnd.next


        index = length - n
        
        i = 0
        while current and i != index:
            current = current.next
            i += 1
        
        current.next = current.next.next

        return dummy.next

        