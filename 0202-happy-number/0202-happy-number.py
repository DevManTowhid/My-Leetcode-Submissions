class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        results = {}
        digits = list(str(n))

        digits = [int(p) ** 2 for p in digits]
        k = sum(digits)
        if k == 1:
            return True
        while k != 1:
            digits = list(str(k))

            digits = [int(p) ** 2 for p in digits]
            k = sum(digits)
            print(k)
            if k == 1:
                return True
            if k in results.keys():
                return False
            results[k] = True
        

        