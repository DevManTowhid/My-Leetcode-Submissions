class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Dictionary to store previously computed results
        memo = {}
        
        def dfs(s1, s2):
            # 1. Check Cache
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            # 2. Base Case: Exact Match
            if s1 == s2:
                return True
            
            # 3. Pruning Step: Character counts must match
            # (Sorting is a quick way to check this in Python)
            if sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            
            n = len(s1)
            
            # 4. Recursive Step: Try splitting at every index
            for i in range(1, n):
                # Case 1: The substrings were NOT swapped
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                
                # Case 2: The substrings WERE swapped
                # s1 left compares to s2 right, s1 right compares to s2 left
                if dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True
            
            # If no valid split is found, they are not scrambles
            memo[(s1, s2)] = False
            return False
            
        return dfs(s1, s2)