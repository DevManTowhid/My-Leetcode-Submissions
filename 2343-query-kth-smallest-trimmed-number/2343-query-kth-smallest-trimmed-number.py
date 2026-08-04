class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        b = [y for x, y in queries]
   
        res =[ ["" for p in nums] for q in range(max(b))]
        
        for i in range(max(b)):
            res[i] = [int(p[-(i + 1):]) for p in nums]
            res[i] = [index for index, _ in sorted(enumerate(res[i]), key=lambda x: x[1] )]

        ans = [[] for p in range(len(queries))]
        for x, y in enumerate(queries):
            # print(y[0], y[0] - 1)
            ans[x] = res[y[1] - 1][y[0] - 1]
  
        return ans
        