# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        rstack = []
        lstack = []

        lstack.append(root.left)
        rstack.append(root.right)

        while rstack and lstack:

            if len(rstack) != len(lstack):
                return False

            noder = rstack.pop()
            nodel = lstack.pop()

            if not noder and not nodel:
                continue
            
            if not noder or not nodel or noder.val != nodel.val:
                return False
            
            
            rstack.append(noder.right)
            rstack.append(noder.left)
            
            lstack.append(nodel.left)
            lstack.append(nodel.right)

        return True
        
