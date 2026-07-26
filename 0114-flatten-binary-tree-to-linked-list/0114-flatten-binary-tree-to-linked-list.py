# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens the binary tree into a linked list in-place.
        The linked list should follow the preorder traversal.
        """
        if not root:
            return
        
        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store the right subtree
        temp_right = root.right
        
        # Move the flattened left subtree to the right
        root.right = root.left
        root.left = None  # Set left to None as per problem requirement
        
        # Find the tail of the new right subtree
        current = root
        while current.right:
            current = current.right
        
        # Attach the original right subtree
        current.right = temp_right