#!/usr/bin/env python3

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n_rows, n_cols = len(board), len(board[0])

        def dfs(r, c):
            if (
                min(r, c) < 0
                or r == n_rows
                or c == n_cols
                or board[r][c] != 'O'
            ):
                return
            board[r][c] = '#'
            neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for x, y in neighbors:
                dfs(x, y)

        for i in range(n_rows):
            for j in range(n_cols):
                if ( (i in {0, n_rows-1} or j in {0, n_cols-1})
                     and board[i][j] == 'O' ):
                     dfs(i, j)
        
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                    
