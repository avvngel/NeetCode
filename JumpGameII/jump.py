#!/usr/bin/env python3

class Solution:
    def jump(self, nums: List[int]) -> int:
        count, l, r = 0, 0, 0
        maxjump = nums[0]
        while r < len(nums)-1:
            for i in range(l, r+1):
                if i+nums[i] > r:
                    maxjump = max(i+nums[i], maxjump)
            l = r+1
            r = maxjump
            count += 1
        return count

