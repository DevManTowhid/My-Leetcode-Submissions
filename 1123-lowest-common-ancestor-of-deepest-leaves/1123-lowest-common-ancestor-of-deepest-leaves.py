# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs_b_t(root):
          
            if not root:
                return [0, None]
            left_sub = dfs_b_t(root.left)
            right_sub = dfs_b_t(root.right)
            if left_sub[0] == right_sub[0]:
                common = root
                
            elif left_sub[0] > right_sub[0]:
                common = left_sub[1]
            elif left_sub[0] < right_sub[0]:
                common = right_sub[1]

            return [1 + max(left_sub[0], right_sub[0]), common]
        
        main = dfs_b_t(root)
        print(main[1].val)
        return main[1]

