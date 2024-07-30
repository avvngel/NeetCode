#!/usr/bin/env python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))    
    def rob1(self, nums: List[int]) -> int:
        prev1, prev2, ans = 0, 0, 0
        for num in nums:
            ans = max(prev1, num + prev2)
            prev2, prev1 = prev1, ans
        return ans


