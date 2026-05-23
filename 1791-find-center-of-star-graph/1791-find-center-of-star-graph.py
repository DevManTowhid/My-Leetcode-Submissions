class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        f = edges[0]
        s = edges[1]

        for i in f:
            if i in s:
                return i
        
        
        return guess
        