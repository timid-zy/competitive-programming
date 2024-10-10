# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, n: int, preq: List[List[int]], Q: List[List[int]]) -> List[bool]:
        # floyd-warshall
        res = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 0
        
        for a, b in preq:
            res[a][b] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    res[i][j] = min(res[i][j], res[i][k] + res[k][j])
        
        ans = [False] * len(Q)
        for i, (a, b) in enumerate(Q):
            if res[a][b] < float('inf'):
                ans[i] = True
        
        return ans
    