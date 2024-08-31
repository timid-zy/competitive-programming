class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def divideByFour(num):
            if num == 1:
                return True
            elif num < 1:
                return False
            return divideByFour(num/4)
        
        return divideByFour(n)