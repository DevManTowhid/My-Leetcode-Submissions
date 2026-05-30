class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Place every number in its correct index if possible.
        # e.g., the number 5 should go to index 4.
        for i in range(n):
            # While the number is within our valid range (1 to n) 
            # AND it is not already sitting in its correct spot...
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                
                # Swap the number to its correct index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Find the first number that isn't in its correct spot
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If all numbers 1 through n are present, the answer is n + 1
        return n + 1