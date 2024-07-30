#!/usr/bin/env python3

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = []
        combo = []
        
        def dfs(i, total):
            nonlocal nums, soln, combo, target

            if total == target:
                soln.append(combo.copy())
                return

            if total > target or i == len(nums):
                return

            combo.append(nums[i])
            dfs(i, total + nums[i])
            combo.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return soln
