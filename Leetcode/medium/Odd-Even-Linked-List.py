# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenList = ListNode(0)
        oddList = ListNode(0)

        even = evenList
        odd = oddList

        current = head
        count = 1
        while current:
            if count % 2 == 1:
                odd.next = current
                odd = odd.next
            else:
                even.next = current
                even = even.next
            
            current = current.next
            count += 1

        even.next = None
        odd.next = evenList.next

        return oddList.next
        
        


        