class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert list of digits to a number
        num = int(''.join(map(str, digits)))
        # Add one
        num += 1
        # Convert back to list of digits
        return list(map(int, str(num)))
        