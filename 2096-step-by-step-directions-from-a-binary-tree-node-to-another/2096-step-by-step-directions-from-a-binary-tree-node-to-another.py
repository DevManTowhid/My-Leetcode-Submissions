# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # Helper function using backtracking to build the path in-place
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            
            # Try left child
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop() # Backtrack if target is not in the left subtree
            
            # Try right child
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop() # Backtrack if target is not in the right subtree
            
            return False

        # Find paths from root to both nodes
        root_to_source = []
        root_to_dest = []
        
        findPath(root, startValue, root_to_source)
        findPath(root, destValue, root_to_dest)
        
        # Find the Lowest Common Ancestor (LCA) by skipping the common prefix
        i = 0
        while i < len(root_to_source) and i < len(root_to_dest) and root_to_source[i] == root_to_dest[i]:
            i += 1
            
        # Everything left in root_to_source needs to be an "Up" ('U') movement
        # Everything left in root_to_dest remains as 'L' or 'R'
        up_moves = 'U' * (len(root_to_source) - i)
        down_moves = "".join(root_to_dest[i:])
        
        return up_moves + down_moves