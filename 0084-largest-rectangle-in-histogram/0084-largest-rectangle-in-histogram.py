class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        s = []
        
        # Right smaller value
        for i in range(n - 1, -1, -1):
            while len(s) > 0 and heights[s[-1]] >= heights[i]:
                s.pop()
            
            right[i] = n if len(s) == 0 else s[-1]
            s.append(i)

        # Clear the stack for the next pass
        s.clear()

        # Left smaller value 
        for i in range(n):
            while len(s) > 0 and heights[s[-1]] >= heights[i]:
                s.pop()
            
            left[i] = -1 if len(s) == 0 else s[-1]
            s.append(i)
            
        ans = 0

        # Calculate maximum area
        for i in range(n):
            area = heights[i] * (right[i] - left[i] - 1)
            ans = max(ans, area)
            
        return ans