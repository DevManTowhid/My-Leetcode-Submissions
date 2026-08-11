# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        digits = []
        def dfs(root, dig):
            if not root: return
            if not root.left and not root.right:
                digits.append(int(dig + str(root.val)))
                return
            dig = dig + str(root.val)
            dfs(root.left, dig)
            dfs(root.right, dig)
        if not root: return 0
        dfs(root, "")
        print(digits)
        return sum(digits)
        