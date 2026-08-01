# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BSTValid(root):
            
            if not root:
                return [True, float('inf'), float('-inf')]


            leftRes = BSTValid(root.left)
            rightRes = BSTValid(root.right)

            if leftRes[0] and rightRes[0] and root.val < rightRes[1] and root.val > leftRes[2]:
                return [True, min(root.val, rightRes[1], leftRes[1] ), max(root.val, rightRes[2], leftRes[2] )]
            else:
                return [False, min(root.val, rightRes[1], leftRes[1] ), max(root.val, rightRes[2], leftRes[2] )]
        
        return BSTValid(root)[0]