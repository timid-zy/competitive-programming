# Problem: Number of Ways to reconstruct a Tree - https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        def dfs(node, set_):
            res = 1
            for nb in graph[node]:
                if nb == node:
                    continue

                if nb not in set_:
                    return 0
                
                if graph[nb] == graph[node]:
                    res = 2
                
                graph[nb].remove(node)
            
            cands = []
            for nb in graph[node]:
                if nb != node: cands.append((len(graph[nb]), nb))
            
            cands.sort()
            for length, nb in reversed(cands):
                if length >= 2 and length == len(graph[nb]):
                    child_res = dfs(nb, set_ & graph[nb])
                    if child_res == 0:
                        return 0
                    elif child_res == 2:
                        res = 2
                    
            return res

        graph = defaultdict(set)
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)
        
        for node in graph:
            graph[node].add(node)

        for node in graph:
            if len(graph[node]) == len(graph):
                return dfs(node, graph[node])
        
        return 0
