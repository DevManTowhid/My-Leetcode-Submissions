# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order must be sorted/ ig
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.ans.append(root.val)
            inorder(root.right)

        self.ans = []
        inorder(root)
        # just check bst main rule that ;left < root < right
        for i in range(1, len(self.ans)):
            if self.ans[i] <= self.ans[i - 1]:
                return False
        return True