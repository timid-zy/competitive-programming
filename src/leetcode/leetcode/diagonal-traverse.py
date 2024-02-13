class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_row = len(mat)
        num_col = len(mat[0])
        
        diagonals = num_row + num_col - 1
        arr = []
        for i in range(diagonals):
            start_row = i
            start_col = 0
            if start_row > num_row - 1:
                start_row = num_row - 1
                start_col = i - start_row
            temp_arr = []
            while start_row >= 0 and start_col < num_col:
                temp_arr.append(mat[start_row][start_col])
                start_row -= 1
                start_col += 1
            # reverse array if diagonal number is odd
            if i % 2 == 1:
                temp_arr = temp_arr[::-1]
            arr += temp_arr
        
        return arr