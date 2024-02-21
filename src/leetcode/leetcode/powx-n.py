class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == float(1) or x == float(0): return x
        if n == 0: return 1

        def customPow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                return customPow(x ** 2, n // 2)
            else:
                return customPow(x ** 2, n // 2) * x

        return customPow(x, n) if n > 0 else customPow(1/x, abs(n))