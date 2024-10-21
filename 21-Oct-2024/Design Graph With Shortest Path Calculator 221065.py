# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(dict)
        for u, v, w in edges:
            self.graph[u][v] = w

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u][v] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        D = defaultdict(lambda: float('inf'))
        D[node1] = 0
        seen = set()
        while heap:
            cd, cn = heappop(heap)
            if cn in seen:
                continue
            
            seen.add(cn)
            for nb in self.graph[cn]:
                nwd = cd + self.graph[cn][nb]
                if nwd < D[nb]:
                    D[nb] = nwd
                    heappush(heap, (nwd, nb))
        
        return D[node2] if D[node2] != float('inf') else -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)