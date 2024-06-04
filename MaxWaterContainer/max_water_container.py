#!/usr/bin/env python3

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            h_l, h_r = heights[l], heights[r]
            area = min(h_l, h_r)*(r - l)
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
