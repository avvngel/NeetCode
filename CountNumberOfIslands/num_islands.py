#!/usr/bin/env python3

class Solution:
    def numIslands_iterative(self, grid: List[List[str]]) -> int:
    """
    Iterative Solution
    """
        n_islands = 0
        visited = set()

        def dfs(r, c):
            nonlocal grid, visited
            stack = [(r, c)]
            while stack:
                i, j = stack.pop()
                if (i, j) in visited:
                    continue
                
                visited.add((i, j))                
                if grid[i][j] == "1":
                    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    for x, y in neighbors:
                        if (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                            stack.append((x, y))
    


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    n_islands += 1
                    dfs(i, j)
        return n_islands

    def numIslands_recursive(self, grid: List[List[str]]) -> int:
    """
    Recursive Solution
    """
        n_islands = 0
        visited = set()
        
        def dfs(i, j):
            nonlocal grid, visited

            if ( (i, j) in visited
                 or i < 0 or i == len(grid)
                 or j < 0 or j == len(grid[0]) 
                 or grid[i][j] == '0'):
                return False
            
            visited.add((i, j))
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for x, y in neighbors:
                dfs(x, y)
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j):
                    n_islands += 1
                    
        return n_islands
