class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                break
        lb, ub = 0, len(row) - 1

        while lb <= ub:
            guess = lb + (ub - lb)//2
            if row[guess] < target:
                lb = guess + 1
            elif target < row[guess]:
                ub = guess - 1
            else:
                return True
        return False
            
            
