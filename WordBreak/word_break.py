#!/usr/bin/env python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False]*(len(s)+1)
        memo[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i+len(word) <= len(s)
                    and word == s[i: i+len(word)]):
                    memo[i] = memo[i+len(word)]
                if memo[i]:
                    break
        return memo[0]
                    
            
        

