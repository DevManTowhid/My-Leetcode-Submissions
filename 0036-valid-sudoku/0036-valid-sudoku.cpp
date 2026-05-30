#include <vector>
#include <unordered_set>

class Solution {
public:
    bool checkforcolumn(vector<vector<char>>& board, int j) {
        unordered_set<char> number;
        for (int i = 0; i < 9; i++) {
            if (board[i][j] != '.') {
                if (!number.insert(board[i][j]).second)
                    return false;
            }
        }
        return true;
    }
    
    bool checkforrow(vector<vector<char>>& board, int i) {
        unordered_set<char> number;
        for (int j = 0; j < 9; j++) {
            if (board[i][j] != '.') {
                if (!number.insert(board[i][j]).second)
                    return false;
            }
        }
        return true;
    }
    
    bool checkforsubbox(vector<vector<char>>& board, int startRow, int startCol) {
        unordered_set<char> number;
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board[i][j] != '.') {
                    if (!number.insert(board[i][j]).second)
                        return false;
                }
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            if (!checkforrow(board, i))
                return false;
        }
        
        for (int j = 0; j < 9; j++) {
            if (!checkforcolumn(board, j))
                return false;
        }
        
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                if (!checkforsubbox(board, i, j))
                    return false;
            }
        }
        
        return true;
    }
};
