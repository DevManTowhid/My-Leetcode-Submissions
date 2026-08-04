class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        MAX_TRY = 100000
        prev = n
        for i in range(MAX_TRY):
            if prev == 1:
                return True
            nxt = 0
            while prev > 0:
                nxt += (prev % 10) * (prev % 10)
                prev = prev // 10
            if nxt in seen:
                return False
            seen.add(nxt)
            prev = nxt
        return False
        