class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def get_lps(st):
            lps = [0] * len(st)
            prev, i = 0, 1
            while i < len(lps):
                if st[prev] == st[i]:
                    prev += 1
                    lps[i] = prev
                    i += 1
                elif prev == 0:
                    i += 1
                else:
                    prev = lps[prev - 1]

            return lps
        

        N = len(s)
        commons = N - get_lps(s+"."+s[::-1])[-1]
        if commons == 0:
            return s

        return s[-commons:][::-1] + s
        