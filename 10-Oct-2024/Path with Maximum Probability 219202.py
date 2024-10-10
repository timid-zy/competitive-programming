# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, E: List[List[int]], P: List[float], st: int, en: int) -> float:
        graph = defaultdict(list)
        for i in range(len(E)):
            graph[E[i][0]].append((E[i][1], P[i]))
            graph[E[i][1]].append((E[i][0], P[i]))

        D = [float('-inf')] * n
        D[st] = 0
        seen = set()
        fringe = [(-1, st)]
        while fringe:
            cp, cn = heappop(fringe)
            if cn in seen:
                continue
            
            if cn == en:
                return -cp
            
            seen.add(cn)
            for nb, pr in graph[cn]:
                newd = cp * pr
                if -newd > D[nb]:
                    D[nb] = -newd
                    heappush(fringe, (newd, nb))
        
        return 0