# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_nums = ListNode(0)
        odd_nums = ListNode(0)

        even = even_nums
        odd = odd_nums

        current = head
        count = 1

        while current:
            if count % 2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            current = current.next
            count += 1

        even.next = None
        odd.next = even_nums.next

        return odd_nums.next

        