#!/usr/bin/env python3

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def helper(i):
            nonlocal s, memo

            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0

            memo[i] = helper(i+1)
            if i < len(s)-1 and (
                s[i] == '1' 
                or s[i] == '2' 
                and s[i+1] in '0123456'
                ):
                memo[i] += helper(i+2)

            return memo[i]

        return helper(0)

