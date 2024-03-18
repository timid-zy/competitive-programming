class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()
        ans = 0
        for i in range(len(houses)):

            nxt = bisect_left(heaters, houses[i])
            dist = abs(houses[i] - heaters[nxt - 1])
            if nxt < len(heaters):
                dist = min(abs(heaters[nxt] - houses[i]), dist)
            
            ans = max(dist, ans)
        
        return ans