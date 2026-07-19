class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        def depth_sum(node):
            # Base case: if we hit a null space, return an empty list of sums
            if not node: 
                return []
            
            # Recursively get the lists of sums from left and right children
            left_sums = depth_sum(node.left)
            right_sums = depth_sum(node.right)
            
            # Combine the lists from both subtrees
            childrens = left_sums + right_sums
            
            # If both are empty, it means this node is a leaf
            if not childrens:
                return [node.val]
            
            # Add the current node's value to all paths coming from the leaves
            sums_up = [child_sum + node.val for child_sum in childrens]
            
            return sums_up

        # Get all possible leaf-to-root path sums
        all_path_sums = depth_sum(root)
        
        # Check if our target matches any of the calculated sums
        return any(num == targetSum for num in all_path_sums)