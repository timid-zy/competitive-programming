# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            indeg[y] += 1
        
        queue = deque()
        for i in range(n):
            if indeg[i] == 0:
                queue.append((i))
        
        res = [set() for _ in range(n)]
        while queue:
            curr = queue.popleft()
            for nb in graph[curr]:
                for a in res[curr]:
                    res[nb].add(a)

                res[nb].add(curr)
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    queue.append(nb)
        
        return [sorted(list(a)) for a in res]