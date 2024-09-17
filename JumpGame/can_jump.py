#!/usr/bin/env python3

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if max_idx <= i+nums[i]:
                max_idx = i
        return not max_idx
