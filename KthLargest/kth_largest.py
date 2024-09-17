#!/usr/bin/env python3

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = self.heapify(nums), k

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.bubble_up(len(self.heap)-1, self.heap)
        
        while self.k < len(self.heap) - 1:
            self.pop(self.heap)
            
        return self.heap[1]

    def pop(self, lst):
        res = lst[1]
        lst[1] = lst.pop()
        self.bubble_down(1, lst)
        return res

    def heapify(self, lst):
        lst = ['#'] + lst
        for i in range(len(lst)//2, 0, -1):
            self.bubble_down(i, lst)
        return lst

    def bubble_up(self, i, lst):
        while 0 < i//2 and lst[i] < lst[i//2]:
            lst[i], lst[i//2] = lst[i//2], lst[i]
            i = i//2
    
    def bubble_down(self, i, lst):
        while i*2 < len(lst):
            if ( i*2 + 1 < len(lst) 
                 and lst[i*2+1] < lst[i*2]
                 and lst[i*2+1] < lst[i] ):
                lst[i], lst[i*2+1] = lst[i*2+1], lst[i]
                i = i*2 + 1
            elif lst[i*2] < lst[i]:
                lst[i], lst[i*2] = lst[i*2], lst[i]
                i *= 2
            else:
                break
                
