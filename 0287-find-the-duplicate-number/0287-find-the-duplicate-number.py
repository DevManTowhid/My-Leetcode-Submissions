class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for x, y in enumerate(nums):
            if x == 0: continue
            if y == nums[x - 1]:
                return y
            
            