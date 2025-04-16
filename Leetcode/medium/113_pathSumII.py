# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        bigArr = []
        def dfs(node, sum, path):
            if not node:
                return

            sum+=node.val
            print(sum)
            path.append(node.val)
            if not node.left and not node.right:
                if sum == targetSum:
                    bigArr.append(path[:])
            
            dfs(node.left, sum, path)
            dfs(node.right, sum, path)
            path.pop()
        dfs(root, 0, [])
        return bigArr
            
        
