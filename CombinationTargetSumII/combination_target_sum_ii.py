#!/usr/bin/env python3

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        soln = []
        combo = []
        candidates.sort()

        def dfs(i, total):
            nonlocal candidates, soln, combo, target

            if total == target:
                soln.append(combo.copy())
                return

            if total > target or i == len(candidates):
                return

            combo.append(candidates[i])
            dfs(i+1, total + candidates[i])
            combo.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)            
        dfs(0, 0)
        return soln

