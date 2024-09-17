#!/usr/bin/env python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        max_ending_here = 0

        for num in reversed(nums):
            max_ending_here = max(num, num + max_ending_here)
            global_max = max(global_max, max_ending_here)
            
        return global_max


