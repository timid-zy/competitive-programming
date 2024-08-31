class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            to_finish = 0
            for i in range(len(piles)):
                to_finish += math.ceil(piles[i] / speed)
            
            return to_finish <= h
        
        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l