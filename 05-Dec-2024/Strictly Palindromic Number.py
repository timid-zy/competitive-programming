class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def get_rep(num, base):
            bt = 1
            while num >= bt:
                bt *= base

            bt //= base
            res = []
            while bt > 0:
                c = num // bt
                res.append(c)
                num -= c * bt
                bt //= base
            
            return res
        
        def is_palindrome(st):
            l, r = 0, len(st)-1
            while l < r:
                if st[l] == st[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True
        
        for b in range(2, n-1):
            if not is_palindrome(get_rep(n, b)):
                return False
        
        return True
