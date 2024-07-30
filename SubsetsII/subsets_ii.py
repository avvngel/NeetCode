#!/usr/bin/env python3
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        soln = []
        subset = []
        nums.sort()

        def dfs(i):
            nonlocal nums, soln, subset

            if i == len(nums):
                soln.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return soln


