class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        maximum = (10 ** n) - 1
        minimum = 10 ** (n - 1)
        
        # Instead of pre-generating a list, we evaluate them sequentially
        for i in range(maximum, minimum - 1, -1):
            # Generate the palindrome on the fly
            text = str(i)
            number = int(text + text[::-1])
            
            # Check for valid factors immediately
            for divisor in range(maximum, minimum - 1, -1):
                # Optimization 1: Break if the factors start repeating
                if divisor * divisor < number:
                    break
                
                if number % divisor == 0:
                    p = number // divisor
                    
                    if p > maximum: 
                        break
                    if p >= minimum:
                        return number % 1337
                        
        return 0