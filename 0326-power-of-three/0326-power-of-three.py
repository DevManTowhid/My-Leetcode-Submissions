class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3 and n != 1:
            return False
        
        def fun(n):
            if n == 3 or n == 1:
                return True
            elif n % 3 != 0:
                return False
            
            return fun(n // 3)
            
        return fun(n)
        