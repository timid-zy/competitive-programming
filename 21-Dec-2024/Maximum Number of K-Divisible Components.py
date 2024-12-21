class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent=None):
            nonlocal components
            if len(graph[node]) == 1 and parent != None:
                if values[node] % k == 0:
                    components += 1
                    return -1

                return values[node]

            curr = values[node]
            for nb in graph[node]:
                if nb == parent:
                    continue

                curr += max(dfs(nb, node), 0)
            
            if curr % k == 0:
                components += 1
                return -1
            
            return curr
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        components = 0
        dfs(0)
        return components