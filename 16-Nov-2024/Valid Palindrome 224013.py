# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and (not (0 <= ord(s[l]) - ord('a') <= 25) and s[l] not in "0123456789"): l += 1
            while l < r and (not (0 <= ord(s[r]) - ord('a') <= 25) and s[r] not in "0123456789"): r -= 1
            if l > r: break
            
            if s[l] != s[r]:
                return False
            
            l += 1; r -= 1

        return True