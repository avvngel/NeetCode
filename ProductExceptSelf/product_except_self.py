#!/usr/bin/env python3

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(len(nums)-1):
            ans.append(ans[i]*nums[i])

        postfix = 1

        for i in range(len(ans)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans


