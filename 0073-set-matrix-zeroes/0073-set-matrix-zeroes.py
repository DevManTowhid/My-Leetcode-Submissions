class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero = set()
        cols_to_zero = set()

        # Step 1: Find all cells that are originally zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        # Step 2: Zero out entire rows
        for r in rows_to_zero:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0

        # Step 3: Zero out entire columns (but skip rows already zeroed)
        for c in cols_to_zero:
            for i in range(len(matrix)):
                if i not in rows_to_zero:  # only change rows that weren't already modified
                    matrix[i][c] = 0
