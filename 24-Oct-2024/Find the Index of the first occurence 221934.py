# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        if len(needle) > len(haystack):
            return -1

        aks = [1] * len(needle)
        aks[-1] = 1
        for i in range(len(aks) - 2, -1, -1):
            aks[i] *= aks[i+1] * 27

        target = curr = 0
        MOD = 10 ** 9 + 7
        for i in range(len(needle) - 1, -1, -1):
            target = (target + (ord(needle[i]) - ord('a') + 1) * aks[i]) % MOD
            curr = (curr + (ord(haystack[i]) - ord('a') + 1) * aks[i]) % MOD

        if target == curr:
            return 0

        for i in range(1, len(haystack) - len(needle) + 1):
            nd = i + len(needle) - 1

            # remove
            curr = (curr - (ord(haystack[i-1]) - ord('a') + 1) * aks[0]) % MOD 
            
            # add
            curr = (curr * 27) % MOD
            curr += (ord(haystack[nd]) - ord('a') + 1)

            if curr == target:
                return i

        return -1

