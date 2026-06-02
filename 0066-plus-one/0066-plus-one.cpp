#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        int n = digits.size();
        
        // Traverse the digits from the end to the beginning
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                // If the digit is less than 9, just increment and return
                digits[i]++;
                return digits;
            }
            // If the digit is 9, it becomes 0 and we continue to the carry
            digits[i] = 0;
        }
        
        // If we reach here, it means all digits were 9 (e.g., 999 -> 000)
        // We need to add a 1 at the beginning
        digits.insert(digits.begin(), 1);
        return digits;
    }
};