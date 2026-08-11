from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def gcd_array(i, current):
            if i == len(nums):
                return current

            return gcd_array(i + 1, gcd(current, nums[i]))

        return gcd_array(1, nums[0]) == 1