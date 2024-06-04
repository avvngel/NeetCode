#!/usr/bin/env python3

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
    """
    O(26n)
    """
        from collections import defaultdict

        char_counts = defaultdict(int)
        l = 0
        max_freq = 0
        ans = 0

        for r in range(len(s)):
            char_counts[s[r]] += 1            

            substr_len = r - l + 1
            n_chars_to_replace = substr_len - max(char_counts.values())

            if n_chars_to_replace <= k:
                ans = substr_len
            else:
                char_counts[s[l]] -= 1
                l += 1

        return ans


    def characterReplacementFaster(self, s: str, k: int) -> int:
    """
    This is the faster solution O(n)
    """
        from collections import defaultdict

        char_counts = defaultdict(int)
        l = 0
        max_freq = 0
        ans = 0
        
        for r in range(len(s)):
            char_counts[s[r]] += 1            
            max_freq = max(char_counts[s[r]], max_freq)

            substr_len = r - l + 1
            n_chars_to_replace = substr_len - max_freq

            if n_chars_to_replace <= k:
                ans = substr_len
            else:
                char_counts[s[l]] -= 1
                l += 1

        return ans

