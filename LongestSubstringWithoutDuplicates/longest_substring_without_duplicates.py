#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        max_len = 0
        substr_chars = set()

        for i in range(len(s)):
            while s[i] in substr_chars:
                substr_chars.remove(s[head])
                head += 1
            substr_chars.add(s[i])
            max_len = max(len(substr_chars), max_len)

        return max_len
