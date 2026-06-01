from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        # Count the frequencies of characters we need from t
        need = Counter(t)
        window = {}

        # 'have' is how many unique characters in our window meet the required frequency
        # 'required' is the total number of unique characters in t
        have, required = 0, len(need)
        
        # Pointers for our sliding window
        l, r = 0, 0
        
        # To store the result: [window_length, left_bound, right_bound]
        res = [float('infinity'), -1, -1]

        while r < len(s):
            # Add the right character to our window
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # If the character is in t and we have the exact amount needed, increment 'have'
            if char in need and window[char] == need[char]:
                have += 1

            # When our window contains all required characters, try to shrink it
            while have == required:
                # Update our minimum window result
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]

                # Remove the left character from our window
                left_char = s[l]
                window[left_char] -= 1

                # If removing it breaks our valid window, decrement 'have'
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                # Move the left pointer forward to shrink
                l += 1
            
            # Move the right pointer forward to expand
            r += 1

        # If we never found a valid window, return an empty string
        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float('infinity') else ""