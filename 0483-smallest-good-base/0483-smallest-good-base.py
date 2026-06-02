import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        
        # Max possible digits 'm' happens at base k=2 -> log2(n) + 1
        max_m = int(math.log2(n)) + 1
        
        # We loop from the largest possible number of digits down to 2.
        # The first valid base we find is guaranteed to be the smallest base.
        for m in range(max_m, 1, -1):
            
            # Target approximation: k ≈ n^(1 / (m - 1))
            # Using integer math fallback if float precision fluctuates
            k = int(n ** (1 / (m - 1)))
            
            if k >= 2:
                # Safe Integer-only Geometric Sum check:
                # n * (k - 1) == k^m - 1
                if n * (k - 1) == (pow(k, m) - 1):
                    return str(k)
                    
        # Fallback: Every number n can be represented as "11" in base n - 1
        return str(n - 1)