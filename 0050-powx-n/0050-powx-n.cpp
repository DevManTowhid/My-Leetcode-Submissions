class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0)
            return 1.0;

        if (n < 0) {
            x = 1.0 / x;
            // Handle the case where n = INT_MIN since -INT_MIN = INT_MIN, and taking the absolute value would overflow.
            // Therefore, convert n to a positive value and multiply x one more time.
            return n == INT_MIN ? x * myPow(x, -(n + 1)) : myPow(x, -n);
        }

        double temp = myPow(x, n / 2);
        return n % 2 == 0 ? temp * temp : x * temp * temp;
    }
};
    