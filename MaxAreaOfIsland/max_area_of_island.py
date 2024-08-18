#!/usr/bin/env python3

class Solution:
    def maxAreaOfIsland_iterative(self, grid: List[List[int]]) -> int:
    """
    Iterative Solution
    """
        max_area = 0
        visited = set()
        
        def get_island_area(r, c):
            nonlocal grid, visited
            
            stack = [(r, c)]
            area = 0

            while stack:
                (i, j) = stack.pop()
                if (i, j) in visited:
                    continue

                visited.add((i, j))
                if grid[i][j] == 1:
                    area += 1
                    neighbors = [(i+1, j),
                                 (i-1, j),
                                 (i, j+1),
                                 (i, j-1)]

                    for x, y in neighbors:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            stack.append((x, y))
                
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, get_island_area(i, j))
        return max_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        
        def get_island_area(r, c):
            nonlocal grid, visited
            
            if ( (r, c) in visited
                 or not 0 <= r < len(grid)
                 or not 0 <= c < len(grid[0])
                 or grid[r][c] == 0 ):
                return 0

            visited.add((r, c))
            return ( 1 + get_island_area(r-1, c)
                       + get_island_area(r+1, c)
                       + get_island_area(r, c-1)
                       + get_island_area(r, c+1) )
                       

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, get_island_area(i, j))
        return max_area
