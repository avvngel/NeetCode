#!/usr/bin/env python3

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = self.heapify(points)
        k_closest = []
        for _ in range(k):
            k_closest.append(self.pop(points))
        return k_closest

    def dist(self, coord):
        x, y = coord
        return (x**2 + y**2)**(1/2)
        
    def heapify(self, lst):
        lst.append(lst[0])
        lst[0] = '#'
        for i in range((len(lst)-1)//2, 0, -1):
            self.bubble_down(i, lst)
        return lst
    
    def pop(self, lst):
        res = lst[1]
        lst[1] = lst[-1]
        lst.pop()
        self.bubble_down(1, lst)
        return res

    def bubble_down(self, i, lst):
        while i*2 < len(lst):
            if ( i*2+1 < len(lst)
                and self.dist(lst[i*2+1]) < self.dist(lst[i*2]) 
                and self.dist(lst[i*2+1]) < self.dist(lst[i]) ):
                lst[i], lst[i*2 + 1] = lst[i*2 + 1], lst[i]
                i = i*2 + 1
            elif self.dist(lst[i*2]) < self.dist(lst[i]):
                lst[i], lst[i*2] = lst[i*2], lst[i]
                i *= 2
            else:
                break

