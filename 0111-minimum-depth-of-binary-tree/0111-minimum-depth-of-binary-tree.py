# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDEPTH = float('inf')
        
        def dfs(root, d):
            nonlocal  minDEPTH
            if not root: return
            if not root.left and not root.right:
                minDEPTH = min(d + 1, minDEPTH)
                print(root.val, minDEPTH)
            else:
                if root.left: dfs(root.left, d + 1)
                if root.right: dfs(root.right, d + 1)
        
        dfs(root, 0.00)
        return 0 if minDEPTH == float('inf') else int(minDEPTH)   