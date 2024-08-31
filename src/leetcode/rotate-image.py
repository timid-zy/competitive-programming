class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for j in range(len(matrix) // 2):
            for i in range(j, len(matrix) - 1 - j):
                tr = matrix[j][i]
                tl = matrix[i][len(matrix) - 1 - j]
                bl = matrix[len(matrix) - 1 - j][len(matrix) - 1 - i]
                br = matrix[len(matrix) - 1 - i][j]
                matrix[j][i], matrix[i][len(matrix) - 1 - j], matrix[len(matrix) - 1 - j][len(matrix) - 1 - i], matrix[len(matrix) - 1 - i][j] = br, tr, tl, bl