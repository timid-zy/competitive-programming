# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def check_parity(start_val, coloring):
            queue = deque([(start_val, 0)])
            while queue:
                c, color = queue.popleft()
                if coloring[c] != -1:
                    if coloring[c] != color:
                        return False
                    
                    continue
                
                coloring[c] = color
                for nb in graph[c]:
                    queue.append((nb, (color + 1) % 2))
            
            return True

        coloring = [-1] * len(graph)
        for i in range(len(graph)):
            if coloring[i] == -1 and not check_parity(i, coloring):
                return False
        
        return True
    
