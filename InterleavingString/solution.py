#!/usr/bin/env python3

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        memo = {}
        def dfs(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if i == len(s3):
                    return True

            ans = False
            no_match = True
            if j < len(s1) and s3[i] == s1[j]:
                ans = ans or dfs(i+1, j+1, k)
                no_match = False

            if k < len(s2) and s3[i] == s2[k]:
                ans = ans or dfs(i+1, j, k+1)
                no_match = False

            if no_match:
                ans = False                
            memo[(i,j,k)] = ans
            return memo[(i,j,k)]
            
        return dfs(0, 0, 0)
            
            
