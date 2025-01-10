# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)    
        indeg = defaultdict(int)
        for n1, n2 in edges:
            graph[n1].append(n2)
            indeg[n2] += 1
        
        queue = deque()
        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)
            
        ancestors = defaultdict(set)
        while queue:
            curr = queue.popleft()
            for nb in graph[curr]:
                ancestors[nb].add(curr)
                for a in ancestors[curr]:
                    ancestors[nb].add(a)
                    
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    queue.append(nb)
        
        res = []
        for i in range(n):
            res.append(sorted(list(ancestors[i])))
        
        return res
