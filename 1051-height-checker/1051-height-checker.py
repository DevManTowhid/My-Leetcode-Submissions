class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cop = heights.copy()
        cop.sort()
        count  = 0
        for i in range(len(heights)):
            if heights[i] != cop[i]:
                count += 1
        return count
        