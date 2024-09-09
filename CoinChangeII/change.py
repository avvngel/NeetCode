#!/usr/bin/env python3

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev_dp = [1] + [0]*(amount)
        for i in range(len(coins)-1, -1, -1):
            dp = [1] + [0]*(amount)
            for amt in range(1, amount+1):
                dp[amt] = prev_dp[amt]
                if coins[i] <= amt:
                    dp[amt] += dp[amt-coins[i]]
            prev_dp = dp
        return dp[amount]

