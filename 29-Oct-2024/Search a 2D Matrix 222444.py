# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, M: List[List[int]], target: int) -> bool:
        if M[0][0] > target or M[-1][-1] < target:
            return False
        
        l, r = 0, len(M) - 1
        while l < r:
            mid = (r + l + 1) // 2
            if M[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        
        row = l
        l, r = 0, len(M[0]) - 1
        while l < r:
            mid = (r + l + 1) // 2
            if M[row][mid] > target:
                r = mid - 1
            else:
                l = mid
        
        return M[row][l] == target
