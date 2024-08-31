class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = pow(10, 9) + 7
        def customPow(num, m):
            if m == 0:
                return 1
            if m == 1:
                return num
            
            if m % 2 == 0:
                return customPow((num ** 2) % mod, m // 2)
            else:
                return customPow((num ** 2) % mod, m // 2) * num 

        multiplier = 20
        num = n // 2
        if n % 2 == 0:
            return (customPow(20,num)) % (pow(10, 9) + 7)
        else:
            return (customPow(20,num) * 5) % (pow(10, 9) + 7)