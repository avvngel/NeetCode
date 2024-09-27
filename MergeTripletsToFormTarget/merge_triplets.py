#!/usr/bin/env python3
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_match = [False, False, False]
        for triplet in triplets:
            if ( target[0] < triplet[0] 
                 or target[1] < triplet[1] 
                 or target[2] < triplet[2] ):
                 continue
            for j in range(len(target)):
                found_match[j] = found_match[j] or triplet[j] == target[j]
        return found_match[0] and found_match[1] and found_match[2]
