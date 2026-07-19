# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(node, curr_sum):
            if not node:
                return False
            curr_sum += node.val
            if not node.left and not node.right: #leaf
                return curr_sum == targetSum
            found_left = False
            found_right = False
            if node.left:
                found_left = DFS(node.left, curr_sum)
            if node.right:
                found_right = DFS(node.right, curr_sum)
            return found_left or found_right

        return DFS(root, 0)
            


        