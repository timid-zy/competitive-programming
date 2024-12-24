class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def get_diameter(start, graph):
            queue = deque([(start, None)])
            lvl = 0
            r = start
            while queue:
                for _ in range(len(queue)):
                    curr, parent = queue.popleft()
                    for nb in graph[curr]:
                        if nb != parent:
                            r = nb
                            queue.append((nb, curr))
                    
                lvl += 1
            
            return r, lvl-1
        
        g1, g2 = defaultdict(list), defaultdict(list)
        for u, v in edges1: g1[u].append(v); g1[v].append(u)
        for u, v in edges2: g2[u].append(v); g2[v].append(u)
        e1, d11 = get_diameter(0, g1)
        _, d11 = get_diameter(e1, g1)
        e2, d22 = get_diameter(0, g2)
        _, d22 = get_diameter(e2, g2)
        return max(d11, d22, math.ceil(d11/2) + math.ceil(d22 / 2) + 1)
