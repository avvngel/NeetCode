#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if price > buy_price:
                max_prof = max(price - buy_price, max_prof)
            else:
                buy_price = price
        return max_prof
