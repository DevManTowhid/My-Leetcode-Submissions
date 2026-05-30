class Solution:
    def trap(self, height: List[int]) -> int:
 
        # Initialize our two pointers at the outer edges
        left, right = 0, len(height) - 1
        # Track the tallest walls we have seen so far on both sides
        max_left = height[left]
        max_right = height[right]

        total_water = 0

        while left < right:
            if height[left] < height[right]:
                # If current height is taller than our max, it becomes the new max
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    # Otherwise, calculate water trapped and add to total
                    total_water += max_left - height[left]
                
                # Move the left pointer inward
                left += 1
                
            else:
                # Process the right side (it is smaller or equal)
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                
                # Move the right pointer inward
                right -= 1

        return total_water



            
        