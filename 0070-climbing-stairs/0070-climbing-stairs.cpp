class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int first = 1;  // represents ways(i-2)
        int second = 2; // represents ways(i-1)

        for (int i = 3; i <= n; ++i) {
            int third = first + second;
            first = second;
            second = third;
        }

        return second;
    }
};