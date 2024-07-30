#!/usr/bin/env python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = ''
        max_len = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_len < r - l - 1:
                max_pali = s[l+1: r]
                max_len = r - l - 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_len < r - l - 1:
                max_pali = s[l+1: r]
                max_len = r - l - 1

        return max_pali

    

