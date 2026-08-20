class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0 for p in range(2 ** n)]
        for x, y in enumerate(res):
            res[x] = x ^ (x >> 1)
        
        print(res)
        return res
        