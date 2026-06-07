# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = p if p.val < q.val else q
        b = p if q.val < p.val else q

    

        def LCA(root, a, b):
            if root.val == a.val:
                return root
            if root.val == b.val:
                return root
                   
            if root.val < a.val:
                
                return LCA(root.right, a, b)
            if root.val > b.val:
                
                return LCA(root.left, a, b)
            
            if root.val > a.val and root.val < b.val:
                return root
            

        return LCA(root, a, b)

        