#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        unordered_set<char> charSet;
        int left = 0;

        for (int right = 0; right < s.size(); ++right) {
            while (charSet.count(s[right])) {
                // If the character at 'right' is already in the set, move the window's left boundary.
                charSet.erase(s[left]);
                left++;
            }

            // Expand the window by adding the character at 'right'.
            charSet.insert(s[right]);
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};
