#!/usr/bin/env python3

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        task_to_count = Counter(tasks)
        max_heap = self.heapify(list(task_to_count.values()))
        q = deque()
        t = 0

        while len(max_heap) > 1 or q:
            t += 1
            if len(max_heap) > 1:
                remaining = self.pop(max_heap) - 1
                if remaining:
                    q.append((remaining, t+n))
            else:
                t = q[0][1]

            if q and q[0][1] == t:
                remaining, _ = q.popleft()
                self.add(remaining, max_heap)
            
        return t

        
    def heapify(self, lst):
        lst.append(lst[0])
        lst[0] = '#'
        for i in range((len(lst)-1)//2, 0, -1):
            self.bubble_down(i, lst)
        return lst

    def bubble_up(self, i, lst):
        while i//2 > 0 and lst[i//2] < lst[i]:
            lst[i], lst[i//2] = lst[i//2], lst[i]
            i = i//2

    def bubble_down(self, i, lst):
        while i*2 < len(lst):
            if ( i*2+1 < len(lst) 
                 and lst[i*2] < lst[i*2+1]
                 and lst[i] < lst[i*2+1] ):
                lst[i], lst[i*2+1] = lst[i*2+1], lst[i]
                i = i*2+1
            
            elif lst[i] < lst[i*2]:
                lst[i], lst[i*2] = lst[i*2], lst[i]
                i *= 2

            else:
                break

    def pop(self, lst):
        res = lst[1]
        lst[1] = lst[-1]
        lst.pop()
        self.bubble_down(1, lst)
        return res

    def add(self, val, lst):
        lst.append(val)
        self.bubble_up(len(lst)-1, lst)




