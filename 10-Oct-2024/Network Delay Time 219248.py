# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # spfa
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        D = [float('inf')] * (n + 1)
        count = [0] * (n + 1)
        D[k] = 0
        inqueue = [False] * (n + 1)
        queue = deque([k])
        while queue:
            cn = queue.popleft()
            inqueue[cn] = False

            for nb, weight in graph[cn]:
                if D[cn] < float('inf') and D[cn] + weight < D[nb]:
                    D[nb] = D[cn] + weight
                    count[nb] = count[cn] + 1
                    if count[nb] >= n:
                        return -1
                    
                    if not inqueue[nb]:
                        queue.append(nb)
                        inqueue[nb] = True
        
        res = max(D[1:])
        return res if res < float('inf') else -1
