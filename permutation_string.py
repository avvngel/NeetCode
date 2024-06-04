#!/usr/bin/env python3



""" 
    BEFORE YOU LOOK AT THE SOLUTION
    RE-IMPLEMENT THE CHAR_COUNTS WITH 
    FIXED-SIZE ARRAYS
"""



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict, Counter

        s1_counts = Counter(s1)
        s2_counts = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            
            if s2[r] in s1_counts:
                s2_counts[s2[r]] += 1
                
            else: # Reset char count dictionary and left bound
                s2_counts = defaultdict(int)
                l = r
            
            # Check if substr exceeds len of s1
            while r - l + 1 > len(s1_counts):
                if s2[l] in s2_counts: # Update char count dict
                    s2_counts[s2[l]] -= 1
                l += 1 # Shorten from left
                
            if s1_counts == s2_counts:
                    return True

        return False
            

