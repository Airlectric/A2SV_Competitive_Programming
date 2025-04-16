# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = ListNode(val=0,next=head)
        pre, curr = placeholder, head

        while curr and curr.next:
            remaining = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = remaining
            pre.next = second

            pre = pre.next.next
            curr = remaining
       

        return placeholder.next

        
