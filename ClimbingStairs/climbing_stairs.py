#!/usr/bin/env python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        one_step, two_steps = 1, 1
        for i in range(n - 1):
            total = one_step + two_steps
            two_steps = one_step
            one_step = total
        return total
 
        
