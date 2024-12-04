class Solution:
    def appealSum(self, s: str) -> int:
        # for i in range(97, 123):
        #     p = -1
        #     for idx, c in enumerate(s):
        #         if c == chr(i):
        #             p = idx
        #         res += p + 1
        
        res = pos = 0
        p = [-1] * 26
        for i, c in enumerate(s):
            curr = ord(c) - ord('a')
            pos += i - p[curr]
            p[curr] = i
            res += pos

        return res