class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # We will store tuples of (start_index, height)
        
        for i, h in enumerate(heights):
            start = i
            # TRIGGER: The current bar is shorter than the top of the stack.
            # This means the taller bars in the stack cannot expand past 'i'.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area for the popped bar
                max_area = max(max_area, height * (i - index))
                # The current shorter bar can be pulled backward 
                # to replace the space of the popped taller bar
                start = index
                
            stack.append((start, h))
            print(start, h)
        # Clean up any remaining bars that made it to the end of the array
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area