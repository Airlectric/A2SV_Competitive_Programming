# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        detect = []

        while current:
            detect.append(current.val)
            current = current.next
        
        return detect == detect[::-1]

        