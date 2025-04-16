# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        arr3 = []
        result = ListNode()
        tail = result

        num1 = l1
        num2 = l2

        while num1:
            arr1.append(str(num1.val))
            num1 = num1.next

        while num2:
            arr2.append(str(num2.val))
            num2 = num2.next

        int1 = int(''.join(reversed(arr1)))
        int2 = int(''.join(reversed(arr2)))

        int3 = int1 + int2
        num3 = str(int3)

        for i in range(len(num3)-1,-1,-1):
            holder = ListNode(val=int(num3[i]))
            tail.next = holder
            tail = tail.next
        return result.next
        

        
