#!/usr/bin/env python3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        max_ending_here, min_ending_here = 1, 1

        for num in nums:
            tmp = max_ending_here
            max_ending_here = max(tmp*num, min_ending_here*num, num)
            min_ending_here = min(tmp*num, min_ending_here*num, num)
            global_max = max(global_max, max_ending_here)

        return global_max

