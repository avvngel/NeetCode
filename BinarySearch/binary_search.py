#!/usr/bin/env python3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums)-1

        while lb <= ub:
            guess = lb + (ub - lb)//2
            if nums[guess] < target:
                lb = guess+1
            elif target < nums[guess]:
                ub = guess-1
            else:
                return guess
        return -1
