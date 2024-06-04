#!/usr/bin/env python3

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for elem in tokens:               
            if elem == '+':
                nums.append(nums.pop() + nums.pop())
            elif elem == '-':
                b, a = nums.pop(), nums.pop()
                nums.append(a - b)
            elif elem == '*':
                nums.append(nums.pop() * nums.pop())
            elif elem == '/':
                b, a = nums.pop(), nums.pop()
                nums.append(int(a / b))
            else:
                nums.append(int(elem))

        return nums[0]
