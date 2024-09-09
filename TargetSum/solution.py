#!/usr/bin/env python3
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, tgt):
            nonlocal nums, memo
            if (i, tgt) in memo:
                return memo[(i, tgt)]
            elif i == len(nums):
                return 0
            if i == len(nums)-1 and abs(tgt) == nums[i]:
                if nums[i] == 0:
                    return 2
                return 1
            memo[(i, tgt)] = (dfs(i+1, tgt-nums[i]) + dfs(i+1, tgt+nums[i]))
            return memo[(i, tgt)]

        return dfs(0, target)


                
