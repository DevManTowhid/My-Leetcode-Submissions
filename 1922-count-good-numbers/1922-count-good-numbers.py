class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Recursive function for fast modular exponentiation
        def recursive_pow(base: int, exp: int) -> int:
            # Base case
            if exp == 0:
                return 1
            
            # Calculate power for half the exponent
            half_pow = recursive_pow(base, exp // 2)
            
            # If exponent is even
            if exp % 2 == 0:
                return (half_pow * half_pow) % MOD
            # If exponent is odd
            else:
                return (base * half_pow * half_pow) % MOD

        # Calculate how many even and odd positions exist
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        # Get answers using our custom recursive function
        even_choices = recursive_pow(5, even_positions)
        odd_choices = recursive_pow(4, odd_positions)
        
        # Multiply and mod for the final result
        return (even_choices * odd_choices) % MOD