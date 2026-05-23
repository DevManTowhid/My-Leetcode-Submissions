class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        remainder = n
        while remainder > 0:
            digits.append(remainder % 10)
            remainder = remainder // 10
        digits.sort()

        m = len(digits)

        return digits[m - 1] * digits[m - 2] if m > 1 else digits[m - 1]
        