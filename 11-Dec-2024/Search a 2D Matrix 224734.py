# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])
        l, r = 0, N*M - 1
        while l <= r:
            mid = (r + l) // 2
            row, col = divmod(mid, M)
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False