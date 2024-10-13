class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        E, G = {}, defaultdict(list)
        for i, (u, v, cnt) in enumerate(edges):
            G[u].append((v, i))
            G[v].append((u, i))
            E[i] = [0, cnt]

        heap = [(0, 0)]
        seen = set()
        while heap:
            cd, cn = heappop(heap)
            if cn in seen:
                continue
            
            seen.add(cn)
            for nb, eidx in G[cn]:
                if cd + E[eidx][1] < maxMoves:
                    heappush(heap, (cd + E[eidx][1] + 1, nb))
                    E[eidx][0] = E[eidx][1]
                else:
                    diff = maxMoves - cd
                    E[eidx][0] = min(E[eidx][0] + diff, E[eidx][1])

        ans = len(seen)
        for v in E.values():
            ans += v[0]

        return ans 