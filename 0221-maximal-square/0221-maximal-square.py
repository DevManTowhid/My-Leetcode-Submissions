class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for p in matrix[0]] for q in matrix] 
        # print(dp)
        def MaxSQ(i, j):
            if matrix[i][j] == "0": 
                dp[i][j] = 0
                return 0
            else:
                up = dp[i - 1][j] if i != 0 else 0
                left_diagon = dp[i - 1][j - 1] if i != 0 else 0
                
                left = dp[i][j - 1] if j != 0 else 0
                
                dp[i][j] = min(up, left, left_diagon) + 1
                return dp[i][j]
        
        Max_side = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = MaxSQ(i, j)
                Max_side = max(curr, Max_side)
        print(dp)
        return Max_side * Max_side

                
            

        