class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def check(ops, base, diff):
            base -= diff * ops
            if base < 0:
                return False
            
            c = 0
            for i in range(40):
                if base & (1 << i): c += 1
            
            return c <= ops and base >= ops

        for i in range(61):
            if check(i, num1, num2): return i
        
        return -1