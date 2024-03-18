class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        row = matrix[row]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False