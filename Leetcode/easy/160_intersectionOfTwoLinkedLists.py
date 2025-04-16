# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        visited = []

        if currA == currB:
            return currA

        while currA or currB:
            if currA in visited:
                return currA

            if currB in visited:
                return currB

            if currA:
                visited.append(currA)
                currA = currA.next
            if currB:
                visited.append(currB)
                currB = currB.next

            if currA == currB:
                return currA
        return 
    



        
