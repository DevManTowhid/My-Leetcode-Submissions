from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Step 1: We must sort the heaters to allow Binary Search
        heaters.sort()
        
        max_illuminate_radius = 0
        
        # Step 2: Loop through every house
        for house in houses:
            
            # --- MANUAL BINARY SEARCH START ---
            low = 0
            high = len(heaters) - 1
            idx = len(heaters) # Fallback index if house is greater than all heaters
            
            while low <= high:
                mid = (low + high) // 2
                
                if heaters[mid] >= house:
                    idx = mid          # This heater could be our right-side neighbor
                    high = mid - 1     # Try to find a closer one on the left
                else:
                    low = mid + 1      # Look to the right side
            # --- MANUAL BINARY SEARCH END ---
            
            # Now 'idx' is the position where the house would sit among heaters.
            # heaters[idx] is the closest heater on the RIGHT
            # heaters[idx - 1] is the closest heater on the LEFT
            
            # Distance to the right neighbor (if it exists)
            if idx < len(heaters):
                dist_right = heaters[idx] - house
            else:
                dist_right = float('inf')
                
            # Distance to the left neighbor (if it exists)
            if idx > 0:
                dist_left = house - heaters[idx - 1]
            else:
                dist_left = float('inf')
            
            # This house chooses whichever of its two neighbors is closer
            individual_radius = min(dist_left, dist_right)
            
            # The global radius must be large enough for the worst-case house
            if individual_radius > max_illuminate_radius:
                max_illuminate_radius = individual_radius
                
        return max_illuminate_radius