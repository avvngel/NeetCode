#!/usr/bin/env python3

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum %2 != 0:
            return False

        target = nums_sum//2
        table = [False]*(target+1)
        table[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                table[i] = table[i] or table[i-num]
        
        return table[target]
