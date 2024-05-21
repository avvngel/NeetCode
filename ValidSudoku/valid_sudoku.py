#!/usr/bin/env python3

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                elem = board[i][j]
                square = i//3*3 + j//3
                if elem == '.':
                    continue
                if (elem in rows[i]) or (elem in cols[j]) or (elem in squares[square]):
                    return False
                else:
                    rows[i].add(elem)
                    cols[j].add(elem)
                    squares[square].add(elem)
        return True
                


