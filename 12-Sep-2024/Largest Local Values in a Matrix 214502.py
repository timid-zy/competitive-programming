# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[float('-inf')] * (len(grid[0]) - 2) for _ in range(len(grid) - 2)]
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                pr, pc = r-1, c-1
                for i in range(9):
                    res[pr][pc] = max(grid[pr + i//3][pc + i%3], res[pr][pc])
        
        return res
