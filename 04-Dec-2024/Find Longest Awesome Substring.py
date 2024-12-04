class Solution:
    def longestAwesome(self, s: str) -> int:
        dct = {}
        rbc = res = 0
        t = []
        for idx, c in enumerate(s):
            n = int(c)
            rbc ^= (1 << n)
            if rbc not in dct:
                dct[rbc] = idx

            if rbc.bit_count() <= 1:
                res = max(res, idx + 1)
                continue
            
            res = max(res, idx - dct[rbc])
            for i in range(10):
                if rbc & (1 << i) and (rbc ^ (1 << i)) in dct:
                    res = max(res, idx - dct[rbc ^ (1 << i)])
                elif (rbc ^ (1<<i)) in dct:
                    res = max(res, idx - dct[rbc ^ (1 << i)])

        return res