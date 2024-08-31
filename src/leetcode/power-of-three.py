class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def divideByThree(num): 
            if num == 1:
                return True
            elif num < 1:
                return False
            return divideByThree(num / 3)
        
        return divideByThree(n)