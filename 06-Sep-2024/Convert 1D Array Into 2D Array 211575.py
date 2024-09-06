# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n*m: return []
        
        mat = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            r, c = i // n, i % n
            mat[r][c] = original[i]
        
        return mat