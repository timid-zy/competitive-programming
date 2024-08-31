class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        lr, lc, rr, rc = 0, 0, 0, len(mat) - 1
        sum = 0
        for i in range(len(mat)):
            sum += mat[lr][lc] + mat[rr][rc]
            lr += 1
            lc += 1
            rr += 1 
            rc -= 1
        if len(mat) % 2 == 1:
            sum -= mat[len(mat) // 2][len(mat) // 2]
        return sum