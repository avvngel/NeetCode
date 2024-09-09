#!/usr/bin/env python3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            nonlocal memo, word1, word2

            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            # match
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]

            # insert
            count1 = dfs(i, j+1)

            # delete
            count2 = dfs(i+1, j)

            # replace
            count3 = dfs(i+1, j+1)

            memo[(i, j)] = 1 + min(count1, count2, count3)
            return memo[(i, j)]

        return dfs(0, 0)
        

