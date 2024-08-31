class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])

        for row in range(len(grid)):
            row_max[row] = max(grid[row])
        
        for col in range(len(grid[0])):
            max_col = grid[0][col]
            for row in range(1, len(grid)):
                max_col = max(max_col, grid[row][col])
            col_max[col] = max_col

        mat = [[0] * len(grid[0]) for _ in range(len(grid))]

        total_inc = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                total_inc += min(row_max[row], col_max[col]) - grid[row][col]
        return total_inc