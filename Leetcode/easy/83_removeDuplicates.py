from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = ListNode(None, head)
        dup = placeholder

        q = deque()

        while dup != None:
            node = dup
            q.append(node.val)

            if dup.next != None and dup.next.val in q :
                while  node.next.next != None and node.next.val == node.next.next.val:
                    dup.next = node.next
                    node = node.next
                dup.next = node.next.next
            dup = node.next
        return placeholder.next
        





        
