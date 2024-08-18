class Solution:
    def pacificAtlantic_iterative(self, heights: List[List[int]]) -> List[List[int]]:
    """
    Iterative solution
    """
        n_rows, n_cols = len(heights), len(heights[0])
        reaches_pacific = ( {(0, col) for col in range(n_cols)}
                          | {(row, 0) for row in range(n_rows)} )
        reaches_atlantic = ( {(n_rows-1, col) for col in range(n_cols)}
                           | {(row, n_cols-1) for row in range(n_rows)} )
    
        def dfs(r, c, reaches_ocean):
            stack = [(r, c)]
            visited = set()

            while stack:
                i, j = stack.pop()
                
                visited.add((i, j))
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

                for x, y in neighbors:
                    if (
                        0 <= x < n_rows
                        and 0 <= y < n_cols
                        and (x, y) not in visited
                        and heights[i][j] <= heights[x][y]
                    ):
                        reaches_ocean.add((x, y))
                        stack.append((x, y))
                        
        for i, j in list(reaches_pacific):
            dfs(i, j, reaches_pacific)

        for i, j in list(reaches_atlantic):
            dfs(i, j, reaches_atlantic)

        return list(reaches_pacific & reaches_atlantic)
