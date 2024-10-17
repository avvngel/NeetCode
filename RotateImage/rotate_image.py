#!/usr/bin/env python3

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottom = l, r
            for i in range(r-l):
                tmp = matrix[top][l+i]
                matrix[l+i][r], tmp = tmp, matrix[l+i][r]
                matrix[bottom][r - i], tmp = tmp, matrix[bottom][r - i]
                matrix[bottom - i][l], tmp = tmp, matrix[bottom - i][l]
                matrix[top][l+i], tmp = tmp, matrix[top][l+i]

            l += 1
            r -= 1

