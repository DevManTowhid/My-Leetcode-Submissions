# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, position):
            nonlocal left_leaves
            if not node:
                return 
            if not node.left and not node.right and position == 0:
                left_leaves += node.val
            else:
                dfs(node.left, 0)
                dfs(node.right, 1)
        left_leaves =  0
        dfs(root, None)

        return left_leaves
