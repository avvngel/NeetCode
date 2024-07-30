#!/usr/bin/env python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPalis(s, i, i)
            count += self.countPalis(s, i, i+1)
            
        return count

    def countPalis(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
                
