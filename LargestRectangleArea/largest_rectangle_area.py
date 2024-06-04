#!/usr/bin/env python3

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right_bound = [len(heights) for _ in heights]
        left_bound = [-1 for _ in heights]
        enum_heights = list(enumerate(heights))

        # Get next right-neighbor that is smaller
        for idx, height in enum_heights:
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                right_bound[i] = idx
            stack.append((idx, height))

        stack = [] # reset stack
        # Get next left-neighbor that is smaller
        for idx, height in reversed(enum_heights):
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                left_bound[i] = idx
            stack.append((idx, height))
        
        max_area = 0
        for idx, height in enum_heights:
            left_area = (idx - 1 - left_bound[idx])*height
            right_area = (right_bound[idx] - (idx))*height
            area = left_area + right_area
            max_area = max(area, max_area)
        return max_area
