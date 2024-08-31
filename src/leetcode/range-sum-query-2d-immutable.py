class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [0] * len(matrix)
        
        for i in range(len(matrix)):
            self.prefix[i] = [0] * len(matrix[0])
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 and col == 0:
                    self.prefix[0][0] = matrix[0][0]
                elif row == 0:
                    self.prefix[0][col] = self.prefix[0][col - 1] + matrix[0][col]
                elif col == 0:
                    self.prefix[row][0] = self.prefix[row - 1][0] + matrix[row][0]
                else:
                    self.prefix[row][col] =  self.prefix[row-1][col] + self.prefix[row][col - 1] - self.prefix[row - 1][col - 1] + matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        elif row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1 - 1]
        elif col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1 - 1][col2]
        else:
            return self.prefix[row2][col2] - self.prefix[row1 - 1][col2] - self.prefix[row2][col1 - 1] + self.prefix[row1 - 1][col1 - 1]        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)