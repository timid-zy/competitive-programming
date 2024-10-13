class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        res = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 0
        
        for u, v, w in edges:
            res[u][v] = res[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    res[i][j] = min(res[i][j], res[i][k] + res[k][j])
        
        ans, anscount = None, float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if res[i][j] <= distanceThreshold:
                    count += 1
            
            if count <= anscount:
                ans, anscount = i, count
        
        return ans
