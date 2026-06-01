#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return "";
        }

        // Count the frequencies of characters we need from t
        unordered_map<char, int> need;
        for (char c : t) {
            need[c]++;
        }

        unordered_map<char, int> window;
        
        // 'have' is how many unique characters in our window meet the required frequency
        // 'required' is the total number of unique characters in t
        int have = 0;
        int required = need.size();
        
        // Pointers for our sliding window
        int l = 0;
        int r = 0;
        
        // To store the result: min_len (infinity equivalent), and start index
        int min_len = -1; // We use -1 to represent infinity
        int min_start = 0;

        while (r < s.length()) {
            // Add the right character to our window
            char c = s[r];
            window[c]++;

            // If the character is in t and we have the exact amount needed, increment 'have'
            // need.count(c) ensures we only care about characters actually in 't'
            if (need.count(c) && window[c] == need[c]) {
                have++;
            }

            // When our window contains all required characters, try to shrink it
            while (have == required) {
                // Update our minimum window result
                if (min_len == -1 || (r - l + 1) < min_len) {
                    min_len = r - l + 1;
                    min_start = l;
                }

                // Remove the left character from our window
                char left_char = s[l];
                window[left_char]--;

                // If removing it breaks our valid window, decrement 'have'
                if (need.count(left_char) && window[left_char] < need[left_char]) {
                    have--;
                }
                
                // Move the left pointer forward to shrink
                l++;
            }
            
            // Move the right pointer forward to expand
            r++;
        }

        // If min_len was never updated, return an empty string. 
        // Otherwise, extract the substring.
        return min_len == -1 ? "" : s.substr(min_start, min_len);
    }
};