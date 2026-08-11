class Solution:
    def numTrees(self, n: int) -> int:
        
        res = [0 for p in range(n + 1)]
        def dfs(n):
            if n <=1 : 
                res[n] = 1
                return res[n]
            if res[n] != 0: return res[n]
            i = 0
            j = n - 1
            count = 0
            while i <= n -1 and  j>= 0:
                left = dfs(i)
                right = dfs(j)
                count += left * right
                i += 1
                j -= 1
            res[n] = count
            # print(res[n])
            return count

        total = dfs(n)
        
        return total  