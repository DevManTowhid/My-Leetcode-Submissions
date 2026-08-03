from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return root
            
        # 1. First Pass: Calculate the total sum of all nodes at each level
        level_sums = []
        queue = deque([root])
        
        while queue:
            current_level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level_sums.append(current_level_sum)
            
        # 2. Second Pass: Update node values based on parents and level sums
        queue = deque([(root, 0)]) # Store a tuple of (node, level_index)
        root.val = 0 # The root never has cousins
        
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                
                # Calculate the sum of the current parent's children (siblings)
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val
                    
                # Safely update the children's values and add them to the queue
                if node.left:
                    node.left.val = level_sums[level + 1] - sibling_sum
                    queue.append((node.left, level + 1))
                    
                if node.right:
                    node.right.val = level_sums[level + 1] - sibling_sum
                    queue.append((node.right, level + 1))
                    
        return root