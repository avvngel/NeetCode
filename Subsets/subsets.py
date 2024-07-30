#!/usr/bin/env python3

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        soln = []

        def helper(i):
            nonlocal soln, nums

            if i == len(nums):
                soln.append(subset.copy())
                return

            subset.append(nums[i])
            helper(i+1)
            subset.pop()
            helper(i+1)

        helper(0)    
        return soln

            

