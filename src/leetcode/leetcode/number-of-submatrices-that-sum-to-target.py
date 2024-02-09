class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        prefix_mat = [0] * len(matrix)
        for i in range(len(prefix_mat)):
            prefix_mat[i] = [0] * len(matrix[0])
        
        for row in range(len(prefix_mat)):
            for col in range(len(prefix_mat[0])):
                if row == 0 and col == 0:
                    prefix_mat[0][0] = matrix[0][0]
                elif row == 0:
                    prefix_mat[0][col] = prefix_mat[0][col - 1] + matrix[0][col]
                elif col == 0:
                    prefix_mat[row][0] = prefix_mat[row - 1][0] + matrix[row][0]
                else:
                    prefix_mat[row][col] = prefix_mat[row - 1][col] + prefix_mat[row][col - 1] - prefix_mat[row - 1][col - 1]  + matrix[row][col]
          
        def getSum(row1, col1, row2, col2):
            if row1 == 0 and col1 == 0:
                return prefix_mat[row2][col2]
            elif row1 == 0:
                return prefix_mat[row2][col2] - prefix_mat[row2][col1 - 1]
            elif col1 == 0:
                return prefix_mat[row2][col2] - prefix_mat[row1 - 1][col2]
            else:
                return prefix_mat[row2][col2] - prefix_mat[row2][col1 - 1] - prefix_mat[row1 - 1][col2] + prefix_mat[row1 - 1][col1 - 1]

        
        count = 0

        for row1 in range(len(prefix_mat)):
            for row2 in range(row1, len(prefix_mat)):

                sums = {0: 1}
                r_sum = 0
                
                for col2 in range(len(prefix_mat[0])):
                    r_sum = getSum(row1, 0, row2, col2)
                    diff = r_sum - target
                    if diff in sums:
                        count += sums[diff]
                    
                    if r_sum in sums:
                        sums[r_sum] += 1
                    else:
                        sums[r_sum] = 1
                    
        return count
