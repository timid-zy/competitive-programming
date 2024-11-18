class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k == 0:
            return res

        r, st, end, d = k, 0, len(code), 1
        if k < 0:
            r, st, end, d = len(code) + k - 1, len(code) - 1, -1, -1
        
        rs = sum(code[k:]) if k < 0 else sum(code[:k])
        for i in range(st, end, d):
            rs -= code[i]
            rs += code[r]
            r = (r + 1) % len(code) if k > 0 else (r - 1) % len(code)
            res[i] = rs
        
        return res
