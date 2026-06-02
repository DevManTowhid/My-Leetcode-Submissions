#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        int n = word2.size();
        std::vector<int> dp(n + 1);
        
        // Initialize base case for the first row
        for (int j = 0; j <= n; ++j) dp[j] = j;
        
        for (char c1 : word1) {
            int prev = dp[0]; // Stores the "diagonal" value
            dp[0]++;          // Update first column
            for (int j = 1; j <= n; ++j) {
                int temp = dp[j]; // Temp store current value for next iteration's "diagonal"
                if (c1 == word2[j - 1]) {
                    dp[j] = prev;
                } else {
                    dp[j] = 1 + std::min({dp[j], dp[j - 1], prev});
                }
                prev = temp;
            }
        }
        return dp[n];
    }
};