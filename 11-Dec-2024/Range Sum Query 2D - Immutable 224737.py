# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N, M = len(matrix), len(matrix[0])
        self.prefix = [[0] * M for _ in range(N)]
        self.prefix[0][0] = matrix[0][0]
        for r in range(1, N):
            self.prefix[r][0] = self.prefix[r-1][0] + matrix[r][0]
        
        for c in range(1, M):
            self.prefix[0][c] = self.prefix[0][c-1] + matrix[0][c]

        for r in range(1, N):
            for c in range(1, M):
                self.prefix[r][c] = self.prefix[r-1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1] + matrix[r][c]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        
        if row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        
        if col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        
        return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)