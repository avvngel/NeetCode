#!/usr/bin/env python3

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        n_fresh = 0
        n_rows, n_cols = len(grid), len(grid[0])
        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    n_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if not n_fresh:
            return 0
            
        t = -1
        while q and n_fresh:
            for _ in range(len(q)):
                i, j = q.popleft()                
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for x, y in neighbors:
                    if (
                        0 <= x < n_rows
                        and 0 <= y < n_cols
                        and grid[x][y] == 1
                     ):
                        q.append((x, y))

                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        n_fresh -= 1
            t += 1

        return t if not n_fresh else -1


                    
