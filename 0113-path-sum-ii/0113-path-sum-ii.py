# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(root, path, Sum):
            if not root: return
            path_curr = path.copy()
            path_curr.append(root.val)
            new_path = path_curr.copy()
            Sum += root.val
            if not root.left and not root.right:
                if Sum == targetSum:
                    paths.append(new_path)
                else:return
            else:
                dfs(root.left, new_path,Sum )
                dfs(root.right, new_path,Sum )


        dfs(root, [], 0)    

        return paths  
        