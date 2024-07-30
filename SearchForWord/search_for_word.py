#!/usr/bin/env python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
                
        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                if self.dfs(row_idx, col_idx, 0, board, n_rows, n_cols, word):
                    return True
        return False
        
    def dfs(self, row, col, i, board, n_rows, n_cols, word):
        if (  row < 0 or n_rows <= row
            or col < 0 or n_cols <= col
            or i == len(word)
            or word[i] != board[row][col]):
            return False
        
        if i+1 == len(word):
            return True

        board[row][col] = '#'
        found = (self.dfs(row+1, col, i+1, board, n_rows, n_cols, word)
                    or self.dfs(row-1, col, i+1, board, n_rows, n_cols, word)
                    or self.dfs(row, col+1, i+1, board, n_rows, n_cols, word)
                    or self.dfs(row, col-1, i+1, board, n_rows, n_cols, word))
                
        board[row][col] = word[i]
        return found
