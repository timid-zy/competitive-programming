class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dct = defaultdict(int)
        for r in range(len(matrix)):
            dct[tuple(matrix[r])] += 1
            sr = tuple([1 if matrix[r][c] == 0 else 0 for c in range(len(matrix[0]))])
            dct[sr] += 1
        
        return max(dct.values())
