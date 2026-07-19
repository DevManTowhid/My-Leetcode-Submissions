# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def depth_sum(root):
            if not root: return []
            childrens = list(depth_sum(root.right)) + list(depth_sum(root.left))
            if not childrens:
                return [root.val]
            sums_ups = [ int(_) + root.val for _ in list(childrens)]

            return sums_ups

        
        lists = depth_sum(root)

        result = any(num == targetSum for num in lists)

        return result
        
        
