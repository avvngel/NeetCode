#!/usr/bin/env python3

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        area = 0
        while l < r:
            wall = min(max_l, max_r)

            if max_l < max_r:
                area += max(wall - height[l], 0)
                l += 1
                max_l = max(max_l, height[l])
            else:
                area += max(wall - height[r], 0)
                r -= 1
                max_r = max(max_r, height[r])
        return area
