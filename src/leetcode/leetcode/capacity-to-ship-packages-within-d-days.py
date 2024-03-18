class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(cap):
            r_sum = 0
            d = days
            for i in range(len(weights)):                
                if r_sum <= cap and r_sum + weights[i] > cap:
                    d -= 1
                    r_sum = 0
                    if d <= 0: return False 

                r_sum += weights[i]
            
            if d >= 0: return True
            return False
        

        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = l + (r - l) // 2
            if isPossible(mid):
                r = mid 
            else:
                l = mid + 1
        
        return l
        