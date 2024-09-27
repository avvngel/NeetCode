#!/usr/bin/env python3

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        import heapq
        counts = Counter(hand)
        min_heap = list(counts.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            first = min_heap[0]

            for elem in range(first, first + groupSize):
                if elem not in counts:
                    return False

                counts[elem] -= 1

                if not counts[elem]:
                    if elem != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True

