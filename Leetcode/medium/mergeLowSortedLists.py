# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pt1 = list1
        pt2 = list2
        placeholder = ListNode()
        tail = placeholder

        while pt1 and pt2:
            if pt1.val < pt2.val:
                tail.next = pt1
                pt1 = pt1.next
            else:
                tail.next = pt2
                pt2 = pt2.next
            
            tail = tail.next

        if pt1:
            tail.next = pt1
        elif pt2:
            tail.next = pt2

        return placeholder.next



