import sys
from typing import List

# Increase recursion depth just in case the binary tree is heavily skewed
sys.setrecursionlimit(200000)

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        # 1. Build an adjacency list for children
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
            
        max_score = 0
        count = 0
        
        # 2. DFS to compute subtree sizes and node scores
        def dfs(node: int) -> int:
            nonlocal max_score, count
            
            size = 1   # Size of the subtree rooted at `node`
            score = 1  # Score if we remove `node`
            
            # Process all children (could be 0, 1, or 2)
            for child in children[node]:
                child_size = dfs(child)
                size += child_size
                score *= child_size # Multiply by the size of the child's component
                
            # Component 3: the rest of the tree above `node`
            remaining = n - size
            if remaining > 0:
                score *= remaining # Multiply by the parent component size
                
            # 3. Update the global max score and count
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1
                
            return size
            
        dfs(0)
        
        return count