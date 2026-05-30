class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size(), L = 0, R = n-1, T = 0, B = n-1;
        int l = L, r = R, t = T, b = B;
        
        while (l < r) {
            for (int i = 0; i < r - l; i++) {
                int var = matrix[t][l + i];
                matrix[t][l + i] = matrix[b - i][l];
                matrix[b - i][l] = matrix[b][r - i];
                matrix[b][r - i] = matrix[t + i][r];
                matrix[t + i][r] = var;
            }
            l++;
            r--;
            t++;
            b--;
        }
    }
};
