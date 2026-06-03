class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares_set = set()
        for i in range(int(math.isqrt(c)) + 1):
            current_square = i * i
            complement = c - current_square
            
            if complement in squares_set or current_square == complement:
                return True
                
            squares_set.add(current_square)

        return False        