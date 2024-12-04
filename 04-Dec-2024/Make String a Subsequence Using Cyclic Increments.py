class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p2 = 0
        for p1 in range(len(str1)):
            if 0 <= -(ord(str1[p1]) - ord(str2[p2])) % 26 <= 1:
                p2 += 1
            
            if p2 >= len(str2):
                return True
        
        return False