#!/usr/bin/env python3

class Solution:
    
    def findMin(self, nums: List[int]) -> int:
        lb, ub = 0, len(nums) - 1

        while lb <= ub:
            guess = lb + (ub - lb)//2

            if nums[lb] <= nums[ub]: # List is in order or bounds have converged
                return nums[lb]

            elif nums[lb] < nums[guess]: # right has the min
                lb = guess+1

            elif nums[guess] < nums[ub]: # left has the min
                ub = guess

            else: # you have the head and tail of the original sorted list
                return nums[guess+1]

    def findMinSimplified(self, nums: List[int]) -> int:
        """
        Preferred Solution
        """
        lb, ub = 0, len(nums) - 1
        current_min = float('inf')

        while lb < ub:
            guess = lb + (ub - lb)//2
            current_min = min(nums[guess], current_min)

            if nums[ub] < nums[guess]: # right has the min
                lb = guess+1

            else: # Left has the min
                ub = guess-1

        return min(current_min, nums[lb])

            
        

