class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[-1] * n for _ in range(m)]
        
        rev_count = 0
        for row, col in walls:
            mat[row][col] = None
            rev_count += 1
        
        for row, col in guards:
            mat[row][col] = "G"
            rev_count += 1

        for row, col in guards:
            for r in range(row + 1, len(mat)):
                if mat[r][col] is None or mat[r][col] == "G": break
                mat[r][col] += 1
                if mat[r][col] == 0: rev_count += 1

            for r in range(row - 1, -1, -1):
                if mat[r][col] is None or mat[r][col] == "G": break
                mat[r][col] += 1
                if mat[r][col] == 0: rev_count += 1

            for c in range(col + 1, len(mat[0])):
                if mat[row][c] is None or mat[row][c] == "G": break
                mat[row][c] += 1
                if mat[row][c] == 0: rev_count += 1
            
            for c in range(col - 1, -1, -1):
                if mat[row][c] is None or mat[row][c] == "G": break
                mat[row][c] += 1
                if mat[row][c] == 0: rev_count += 1
            
        # for row in range(len(mat)):
        #     for col in range(len(mat[0])):
        #         if mat[row][col] is not None and mat[row][col] == -1:
        #             count += 1
        return m*n - rev_count 