# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0
        seen = set()
        fringe = [(0, k)]
        while fringe:
            cd, cn = heappop(fringe)
            if cn in seen:
                continue
            
            seen.add(cn)

            for nb, weight in graph[cn]:
                if cd + weight < distances[nb]:
                    distances[nb] = cd + weight
                    heappush(fringe, (cd + weight, nb))
        
        res = max(distances.values()) 
        print(distances)
        return res if res != float('inf') else -1
        
        