class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def binarySearch(left, right):
            # Base Case: When left pointer crosses right, 
            # 'left' is the correct insertion index.
            if left > right:
                return left
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is strictly greater, search the right half.
                # Notice the 'return' keyword!
                return binarySearch(mid + 1, right)
            else:
                # Target is strictly smaller, search the left half.
                # Notice the 'return' keyword!
                return binarySearch(left, mid - 1)

        return binarySearch(0, len(nums) - 1)