class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left_to_right = True
        remaining = n
        
        while remaining > 1:
            # The head moves forward if we move left-to-right, 
            # OR if we move right-to-left and the number of elements is odd.
            if left_to_right or remaining % 2 == 1:
                head += step
                
            # Every round, the step size doubles
            step *= 2
            # Every round, the number of remaining elements is cut in half
            remaining //= 2
            # Alternate the direction for the next round
            left_to_right = not left_to_right
            
        return head

