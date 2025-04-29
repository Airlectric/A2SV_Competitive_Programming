# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_head = None

        while current:
            next_ = current.next
            current.next = new_head
            new_head = current
            current = next_

        return new_head
        