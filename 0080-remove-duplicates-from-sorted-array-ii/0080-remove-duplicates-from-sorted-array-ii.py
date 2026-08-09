class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # 'k' points to the position where the next valid element should be placed.
        # The first two elements (index 0 and 1) are always valid.
        k = 2
        
        for i in range(2, len(nums)):
            # Only write nums[i] if it differs from the element 2 steps behind in our modified array
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k