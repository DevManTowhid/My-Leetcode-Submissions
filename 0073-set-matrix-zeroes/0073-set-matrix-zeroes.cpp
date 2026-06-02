#include <vector>
#include <unordered_set>

class Solution {
public:
    void setZeroes(std::vector<std::vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        std::unordered_set<int> rows_to_zero;
        std::unordered_set<int> cols_to_zero;

        // Step 1: Find all cells that are originally zero
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (matrix[i][j] == 0) {
                    rows_to_zero.insert(i);
                    cols_to_zero.insert(j);
                }
            }
        }

        // Step 2: Zero out entire rows
        for (int r : rows_to_zero) {
            for (int j = 0; j < cols; ++j) {
                matrix[r][j] = 0;
            }
        }

        // Step 3: Zero out entire columns
        for (int c : cols_to_zero) {
            for (int i = 0; i < rows; ++i) {
                // If the row was already zeroed, it doesn't hurt to set it to 0 again
                matrix[i][c] = 0;
            }
        }
    }
};