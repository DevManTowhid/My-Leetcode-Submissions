class Solution {
public:
    std::string longestPalindrome(std::string s) {
        int start = 0;
        int max_length = 0;

        for (int i = 0; i < s.length(); i++) {
            // Check for palindromes with the center at s[i]
            int len1 = expandAroundCenter(s, i, i);
            // Check for palindromes with the center between s[i] and s[i+1]
            int len2 = expandAroundCenter(s, i, i + 1);

            int current_length = std::max(len1, len2);
            if (current_length > max_length) {
                max_length = current_length;
                // Calculate the starting index of the palindrome
                start = i - (current_length - 1) / 2;
            }
        }

        // Extract and return the longest palindromic substring
        return s.substr(start, max_length);
    }

private:
    int expandAroundCenter(const std::string& s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        // Return the length of the palindrome centered at s[left] and s[right]
        return right - left - 1;
    }
};