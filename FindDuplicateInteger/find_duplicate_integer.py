#!/usr/bin/env python3

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
    """
    Baby solution
    """
        seen = set()
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] in seen: return nums[l]
            seen.add(nums[l])
            if nums[r] in seen: return nums[r]
            seen.add(nums[r])
            l += 1
            r -= 1

    def findDuplicate(self, nums: List[int]) -> int:
    """
    O(1) space solution
    """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
