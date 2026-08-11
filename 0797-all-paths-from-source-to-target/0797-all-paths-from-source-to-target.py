from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(node, path):
            # Reached target
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            # Explore every neighbor
            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt, path)
                path.pop()

        dfs(0, [0])

        return paths