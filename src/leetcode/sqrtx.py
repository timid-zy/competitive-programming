class Solution:
    def mySqrt(self, x: int) -> int:
        
        i, j = 0, x
        while i <= j:
            mid = i + (j - i) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 >= x:
                if (mid - 1) ** 2 < x:
                    return mid - 1
                j = mid - 1
            
            else:
                i = mid + 1
        
        return i