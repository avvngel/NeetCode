#!/usr/bin/env python3

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ == target:
                return l+1, r+1
            elif sum_ < target:
                l += 1
            else:
                r -= 1
