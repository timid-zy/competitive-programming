# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, P: int, MOD: int, k: int, hashValue: int) -> str:
        s = s[::-1] # avoid using modulo inverses
        aks = [1] * k
        for i in range(k-2, -1, -1):
            aks[i] = (aks[i+1] * P) % MOD
        
        curr = 0
        for i in range(k-1, -1, -1):
            curr = (curr + (ord(s[i]) - 96) * aks[i]) % MOD
        
        ans = ""
        if curr == hashValue:
            ans = s[:k][::-1]

        for i in range(1, len(s) - k + 1):
            nb = i + k - 1
            curr = (curr - aks[0]*(ord(s[i-1]) - 96)) % MOD
            curr = (curr * P) % MOD
            curr = (curr + ord(s[nb]) - 96) % MOD 

            if curr == hashValue:
                ans = s[i:i+k][::-1]
        
        return ans
