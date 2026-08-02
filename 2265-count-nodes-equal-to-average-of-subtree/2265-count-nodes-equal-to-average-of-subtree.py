# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        
        def avg(node):
            nonlocal count  # Allows modification of the outer 'count' variable
            if not node:
                return 0, 0
            
            left_sum, left_nodes = avg(node.left)
            right_sum, right_nodes = avg(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_nodes = left_nodes + right_nodes + 1
            
            # Floor division to round down to nearest integer
            if total_sum // total_nodes == node.val:
                count += 1
                
            return total_sum, total_nodes
        
        avg(root)
        return count