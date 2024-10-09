# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pd = [float('inf')] * (n+1)
        pd[k] = 0

        for _ in range(n-1):
            cd = pd[:]
            for u, v, w in times:
                cd[v] = min(cd[v], cd[u] + w)
            
            pd = cd
        
        res = max(pd[1:])
        return res if res != float('inf') else -1