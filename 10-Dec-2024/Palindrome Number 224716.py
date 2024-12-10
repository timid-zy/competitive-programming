# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rs = 0
        tmp = x
        while tmp != 0:
            digit = tmp % 10
            rs = rs * 10 + digit
            tmp //= 10
        
        return rs == x