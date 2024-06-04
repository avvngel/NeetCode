#!/usr/bin/env python3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solution 1
        """
        set_nums = set(nums)
        visited = set()
        current_seq_len = 0
        max_seq_len = 0
        for num in set_nums:
            if num in visited:
                continue
            current_seq_len += 1
            visited.add(num)
            left_nhb = num - 1
            while left_nhb in set_nums:
                visited.add(left_nhb)
                current_seq_len += 1
                left_nhb -= 1
            right_nhb = num + 1
            while right_nhb in set_nums:
                visited.add(right_nhb)
                current_seq_len += 1
                right_nhb += 1
            max_seq_len = max([current_seq_len, max_seq_len])
            current_seq_len = 0

        return max([current_seq_len, max_seq_len])

    def longestConsecutiveSimple(self, nums: List[int]) -> int:
        """
        Solution 2
        """
        set_nums = set(nums)
        max_seq_length = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                next_num = num + 1
                while next_num in set_nums:
                    length += 1
                    next_num += 1
                max_seq_length = max(length, max_seq_length)
        
        return max_seq_length
            
