class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row_num = len(grid)
        col_num = len(grid[0])
        max_sum = float('-inf')
        for row in range(row_num - 2):
            for col in range(col_num - 2):
                sum = grid[row][col] + grid[row][col + 1] + grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
                max_sum = max(max_sum, sum)
        
        return max_sum