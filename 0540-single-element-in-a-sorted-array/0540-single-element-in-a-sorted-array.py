class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        # We stop when low == high, which will point to the single element
        while low < high:
            mid = (low + high) // 2
            
            # This automatically finds the 'partner' index based on even/odd
            # If mid is even, partner = mid + 1
            # If mid is odd, partner = mid - 1
            partner = mid ^ 1
            
            # If they match, we are on the correct left-side pattern
            if nums[mid] == nums[partner]:
                low = mid + 1  # Move right
            else:
                high = mid     # Move left (mid could still be the single element)
                
        return nums[low]