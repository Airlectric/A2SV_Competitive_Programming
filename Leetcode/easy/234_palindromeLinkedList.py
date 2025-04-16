# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        previous = None

        while curr:
            second = curr.next
            curr.next = previous
            previous = curr
            curr = second

        full, revhalf = head, previous
        
        while revhalf:
            if revhalf.val != full.val:
                return False
            full = full.next
            revhalf = revhalf.next
        
        return True
         
