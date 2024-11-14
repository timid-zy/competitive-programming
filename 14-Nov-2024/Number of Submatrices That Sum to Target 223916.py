# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        N, M = len(matrix), len(matrix[0])
        prefix = [[0] * M for _ in range(N)]
        prefix[0][0] = matrix[0][0]
        for i in range(1, N):
            prefix[i][0] = prefix[i-1][0] + matrix[i][0]
        
        for i in range(1, M):
            prefix[0][i] = prefix[0][i-1] + matrix[0][i]
        
        for r in range(1, N):
            for c in range(1, M):
                prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1] + matrix[r][c]
        
        res = 0
        for r1 in range(N):
            for r2 in range(r1, N):
                dct = defaultdict(int)
                dct[0] = 1
                for c in range(M):
                    curr = prefix[r2][c] - prefix[r1-1][c] if r1 > 0 else prefix[r2][c]
                    t = curr - target
                    res += dct[t]
                    dct[curr] += 1

        return res