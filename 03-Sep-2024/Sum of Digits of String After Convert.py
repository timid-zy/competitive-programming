# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        arr = []
        for c in s: arr.append(ord(c) - 96)

        res = 0
        for n in arr:
            d = n
            for i in range(4, -1, -1):
                c = d // 10**i
                res += c
                d -= c * 10**i

        for i in range(k-1):
            d = res
            res = 0
            for i in range(4, -1, -1):
                c = d // 10**i
                res += c
                d -= c * 10**i
        
        return res
