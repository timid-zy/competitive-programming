# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, W: str) -> int:
        VOWELS = ["a", "e", "i", "o", "u"]
        dp = vs = 1 if W[-1] in VOWELS else 0
        for i in range(len(W)-2, -1, -1):
            p = len(W) - i
            if W[i] in VOWELS:
                dp += p + vs; vs += p
            else:
                dp += vs
        
        return dp