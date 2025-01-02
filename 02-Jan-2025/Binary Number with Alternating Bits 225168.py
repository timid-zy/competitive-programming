# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(n))[2:]
        c = s[0]
        for i in range(1, len(s)):
            if c == s[i]:
                return False
            
            c = s[i]
            
        return True