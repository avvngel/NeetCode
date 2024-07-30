#!/usr/bin/env python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for i in range(len(nums)):
            nums[i] = max(prev1, nums[i] + prev2)
            prev2, prev1 = prev1, nums[i]
        return nums[-1]
