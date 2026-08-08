# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        
        def found(node, target, path):
            if not node:
                return False
            if node == target:
                path.append(node)  # Store the TreeNode object
                return True
            
            if found(node.left, target, path) or found(node.right, target, path):
                path.append(node)  # Store the TreeNode object
                return True
            return False

        found(root, p, p_path)
        found(root, q, q_path)
        
        # Reverse paths to go from root -> target
        p_path.reverse()
        q_path.reverse()
        
        lca = None
        for u, v in zip(p_path, q_path):
            if u == v:
                lca = u
            else:
                break
        return lca