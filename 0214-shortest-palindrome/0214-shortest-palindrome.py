class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        j = 0

        # Find the longest palindromic prefix
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[j]:
                j += 1

        # Entire string is already a palindrome
        if j == len(s):
            return s

        suffix = s[j:]

        return suffix[::-1] + self.shortestPalindrome(s[:j]) + suffix