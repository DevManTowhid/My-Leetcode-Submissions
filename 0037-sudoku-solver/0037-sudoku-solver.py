class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. Initialize arrays of sets to track constraints in O(1) time
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        empty_cells = []

        # 2. Pre-process the board
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c)) # Only track what we need to fill
                else:
                    val = board[r][c]
                    box_index = (r // 3) * 3 + (c // 3)
                    # Add existing numbers to our trackers
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_index].add(val)

        # 3. The Backtracking Function
        def solve(index=0):
            # Base Case: If we've processed all empty cells, we are done!
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)
            
            # Try numbers 1-9
            for val in map(str, range(1, 10)):
                # O(1) validity check using our sets
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_index]:
                    
                    # Place the guess and update our sets
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_index].add(val)
                    
                    # Recurse to the NEXT empty cell
                    if solve(index + 1):
                        return True
                        
                    # THE BACKTRACK: Undo the guess and remove from sets
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_index].remove(val)
                    
            return False

        # Start the recursion from the first empty cell
        solve(0)