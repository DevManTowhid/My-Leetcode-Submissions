#include <string>

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";

        string result = "1";
        for (int i = 2; i <= n; i++) {
            string nextTerm;
            int j = 0;
            int len = result.length();

            while (j < len) {
                char currentDigit = result[j];
                int count = 0;

                // Count the consecutive occurrences of the current digit
                while (j < len && result[j] == currentDigit) {
                    count++;
                    j++;
                }

                // Append the count and digit to the next term
                nextTerm += to_string(count) + currentDigit;
            }

            // Update the result with the next term for the next iteration
            result = nextTerm;
        }

        return result;
    }
};
