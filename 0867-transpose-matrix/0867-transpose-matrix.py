class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # zip(*matrix) unpacks the matrix and pairs the elements by column
        return [list(row) for row in zip(*matrix)]
        