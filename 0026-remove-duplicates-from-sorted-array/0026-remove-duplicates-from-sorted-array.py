class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'k' tracks the index where the next unique element should be placed
        k = 1
        
        for i in range(1, len(nums)):
            # When we find a new unique element, overwrite position 'k'
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k
