class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty, no path can exist
        if not root:
            return False
        
        # Subtract the current node's value from the remaining target
        targetSum -= root.val
        
        # Check if we are at a leaf node (no children)
        if not root.left and not root.right:
            return targetSum == 0
        
        # Recursively check the left and right subtrees
        # Short-circuit evaluation: if the left side returns True, the right side won't even run
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)