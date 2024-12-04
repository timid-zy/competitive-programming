class Solution:
    def countDigitOne(self, n: int) -> int:
        digs = [0, 1]
        for i in range(1, 10):
            digs.append(10 ** i + 10*digs[-1])
        
        res = 0
        i = 9
        for i in range(9, -1, -1):
            d = 10**i
            if d > n: continue
            
            res += min(d, n-d+1)
            res += n//d * digs[i]
            n %= d
        
        return res