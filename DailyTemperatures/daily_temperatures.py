#!/usr/bin/env python3

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in temperatures]
        enum_temp = list(enumerate(temperatures))
        for (i, temp1), (j, temp2) in zip(enum_temp[:-1], enum_temp[1:]):
            while stack and stack[-1][1] < temp2:
                idx, t = stack.pop()
                ans[idx] = j - idx
            if temp1 < temp2:
                ans[i] = 1
            else:
                stack.append((i, temp1))
        return ans

class SimplifiedSolution:
    """
    Simplified Solution
    """
    def dailyTemperaturesSimplified(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in temperatures]
        for (i, temp) in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, t = stack.pop()
                ans[idx] = i - idx
            stack.append((i, temp))
        return ans
