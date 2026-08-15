# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []
        path = []
        sm = 0
        def rec(root):
            nonlocal sm
            if not root:
                return 
            
            sm+=root.val
            path.append(root.val)
            if not root.left and not root.right and sm==targetSum:
                ans.append(path[:])
            rec(root.left)
            rec(root.right)
            sm-=root.val
            path.pop()

        rec(root)
        
        return ans


