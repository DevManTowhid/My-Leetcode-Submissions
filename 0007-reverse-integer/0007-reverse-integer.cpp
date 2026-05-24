class Solution {
public:
    int reverse(int x) {
        int reversed = 0;
        while (x != 0) {
            int digit = x % 10;
            // Checking for potential overflow/underflow
            if (reversed > INT_MAX / 10 || (reversed == INT_MAX / 10 && digit > 7))
                return 0; // Exceeds the upper limit of 32-bit integer
            if (reversed < INT_MIN / 10 || (reversed == INT_MIN / 10 && digit < -8))
                return 0; // Exceeds the lower limit of 32-bit integer

            reversed = reversed * 10 + digit;
            x /= 10;
        }
        return reversed;
    }
};
