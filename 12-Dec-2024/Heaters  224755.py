# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check_radius(r):
            i = h = 0
            while i < len(houses) and h < len(heaters):
                if abs(heaters[h] - houses[i]) <= r:
                    i += 1
                else:
                    h += 1
            
            return i == len(houses)
        
        houses.sort()
        heaters.sort()
        l, r = 0, 10 ** 9 + 1
        while l < r:
            mid = (l + r) // 2
            if check_radius(mid):
                r = mid
            else:
                l = mid + 1
        
        return l