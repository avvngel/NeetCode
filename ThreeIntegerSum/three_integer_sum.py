#!/usr/bin/env python3

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []
        print(nums)
        for i, target in enumerate(nums):
            if i > 0 and nums[i-1] == target:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                partial_sum = nums[l] + nums[r]
                if partial_sum > -target:
                    r -= 1

                elif partial_sum < -target:
                    l += 1

                else:
                    sums.append([target, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return sums




