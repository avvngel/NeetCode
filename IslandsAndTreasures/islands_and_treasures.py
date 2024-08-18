#!/usr/bin/env python3

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        
        q = deque()
        visited = set()
        n_rows, n_cols = len(grid), len(grid[0])
        
        def addCell(i, j):
            if (
                min(i, j) < 0
                or i == n_rows
                or j == n_cols
                or (i, j) in visited
                or grid[i][j] == -1
            ):
                return
            visited.add((i, j))
            q.append((i, j))

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        path_len = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = path_len
                addCell(i-1, j)
                addCell(i+1, j)
                addCell(i, j-1)
                addCell(i, j+1)
                        
            path_len += 1

