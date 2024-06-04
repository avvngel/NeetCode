#!/usr/bin/env python3

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        
        # Constants
        max_val = max(piles)

        # Helper function
        def get_hours_needed(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            return hours

        # Bisection Search
        lb, ub = 1, max_val
        
        k = max_val
        
        while lb <= ub:
            guess = lb + (ub - lb)//2
            hours = get_hours_needed(guess)

            if hours > h: # Check if rate is too slow
                lb = guess + 1

            else: # Check if rate could be slower
                k = guess
                ub = guess - 1
            
        return k
