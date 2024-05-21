#!/usr/bin/env python3

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        ranked_num_counts = [[] for _ in nums]
        num_counts = Counter(nums)
        ans = []

        for num, count in num_counts.items():
            ranked_num_counts[count-1].append(num)

        for group in reversed(ranked_num_counts):

            for num in group:
                ans.append(num)
                if len(ans) == k:
                    return ans


