#!/usr/bin/env python3

class Solution:
    def longestCommonSubsequence_td(self, text1: str, text2: str) -> int:
    """
    Top-Down approach
    """
        memo = {}
        def helper(i, j):
            nonlocal memo
            
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + helper(i+1, j+1)
            else:
                memo[(i, j)] = max(helper(i, j+1), helper(i+1, j))
            return memo[(i, j)]
        return helper(0, 0)

    def longestCommonSubsequence_bu(self, text1: str, text2: str) -> int:
        """
        Bottom-Up approach
        """
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(dp)-2, -1, -1):
            for j in range(len(dp[0])-2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]    
        
