
class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.size(), n = b.size();
        string output;

        // Adding leading zeros to the smaller string
        if (m > n) {
            int diff = m - n;
            b.insert(0, diff, '0');
        } else if (n > m) {
            int diff = n - m;
            a.insert(0, diff, '0');
        }

        int carryIn = 0, carryOut = 0;
        int i = a.size() - 1;

        while (i >= 0) {
            carryIn = carryOut;

            int r = a[i] - '0'; // Convert character to integer (0 or 1)
            int q = b[i] - '0'; // Convert character to integer (0 or 1)

            int sum = carryIn ^ (r ^ q);
            output.insert(0, 1, sum + '0'); // Convert sum to character (0 or 1) and add to the beginning of the output string
            carryOut = (r & q) | (carryIn & (r ^ q));

            i--;
        }

        // Add the final carry bit if there is any
        if (carryOut)
            output.insert(0, 1, '1');

        return output;
    }
};