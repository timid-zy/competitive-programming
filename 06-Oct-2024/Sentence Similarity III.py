class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        i1 = j1 = 0
        while i1 < len(s1) and j1 < len(s2):
            if s1[i1] != s2[j1]:
                break
            
            i1 += 1; j1 += 1
        
        if i1 == len(s1) or j1 == len(s2):
            return True
        
        i2, j2 = len(s1) - 1, len(s2) - 1
        while 0 <= i2 < len(s1) and 0 <= j2 < len(s2):
            if s1[i2] != s2[j2]:
                break
            
            i2 -= 1; j2 -= 1
        
        if i2 == -1 or j2 == -1:
            return True
        
        return i2 < i1 or j2 < j1
