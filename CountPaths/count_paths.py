#!/usr/bin/env python3

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if min(m, n) == 1:
                return 1

        dp = [[0]*(n-1) + [1] + [0] for _ in range(m-1)]
        dp.append([1 for _ in range(n)] + [0])
        dp.append([0]*n)

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

        
