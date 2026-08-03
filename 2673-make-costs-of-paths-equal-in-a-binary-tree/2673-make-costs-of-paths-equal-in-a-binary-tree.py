from typing import List

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        total_increments = 0
        
        # Start from the last parent node and move bottom-up to the root (index 0)
        # The last parent node in a 0-indexed perfect binary tree is at (n // 2) - 1
        for i in range(n // 2 - 1, -1, -1):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            # 1. Add the difference between the two siblings to our operations count
            # This makes the paths through both children equal.
            total_increments += abs(cost[left_child] - cost[right_child])
            
            # 2. Update the parent's cost to include the max path of its children.
            # This bubbles the required path sum up the tree.
            cost[i] += max(cost[left_child], cost[right_child])
            
        return total_increments