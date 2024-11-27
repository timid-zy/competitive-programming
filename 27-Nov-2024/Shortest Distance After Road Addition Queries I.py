from collections import defaultdict, deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i+1)
        
        depth = [i for i in range(n)]

        def bfs(node):
            q = deque([node])
            while q:
                n = q.popleft()
                for nei in adj[n]:
                    if depth[nei] > depth[n]+1:
                        depth[nei] = depth[n]+1
                        q.append(nei)
        
        ans = []
        for s, e in queries:
            adj[s].append(e)
            if depth[e] > depth[s]+1:
                depth[e] = depth[s]+1
                bfs(e)
            ans.append(depth[-1])
        return ans
            