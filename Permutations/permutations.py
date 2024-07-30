#!/usr/bin/env python3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        permutations = []
        permutation = []

        def dfs(permutation, nums_set):
            nonlocal permutations
            
            if not nums_set:
                permutations.append(permutation.copy())
                return

            for num in nums_set:
                permutation.append(num)
                dfs(permutation, nums_set - {num})
                permutation.pop()

        dfs(permutation, nums_set)
        return permutations
                

