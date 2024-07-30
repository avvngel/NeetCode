#!/usr/bin/env python3

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        partition = []

        def helper(i, j):
            nonlocal s, partitions, partition

            if j > len(s):
                if i == len(s):
                    partitions.append(partition.copy())
                return

            if self.isPalindrome(s, i, j-1):
                partition.append(s[i:j])
                helper(j, j+1)
                partition.pop()
            helper(i, j+1)

        helper(0, 1)
        return partitions

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
