#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, buying):
            nonlocal memo

            if (i, buying) in memo:
                return memo[(i, buying)]
            if i >= len(prices):
                return 0

            if buying:
                memo[(i, buying)] = max(helper(i+1, False) - prices[i],
                                        helper(i+1, buying))
            else:
                memo[(i, buying)] = max(helper(i+2, True) + prices[i],
                                        helper(i+1, buying))

            return memo[(i, buying)]

        return helper(0, True)
        

