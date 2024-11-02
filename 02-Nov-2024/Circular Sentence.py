class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
        for i in range(1, len(s)):
            if s[i][0] != s[i-1][-1]:
                return False
        
        return s[0][0] == s[-1][-1]