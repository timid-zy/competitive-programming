# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ds = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ds.append(i)
        
        if ds and len(ds) != 2:
            return False
        
        return not ds or (s1[ds[0]] == s2[ds[1]] and s1[ds[1]] == s2[ds[0]])