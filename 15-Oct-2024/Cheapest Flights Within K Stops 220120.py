# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pd = [float('inf')] * n
        pd[src] = 0
        for _ in range(k+1):
            cd = pd[:]
            for u, v, w in flights:
                cd[v] = min(cd[v], pd[u] + w)
            
            pd = cd
        
        return pd[dst] if pd[dst] < float('inf') else -1