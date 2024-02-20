class Solution:
    def minimumSteps(self, s: str) -> int:
        
        blackPos = len(s) - 1
        while blackPos >= 0 and s[blackPos] == "1":
            blackPos -= 1
        
        i = blackPos
        steps = 0
        while i >= 0:
            if s[i] == "1":
                steps += blackPos - i
                blackPos -= 1
            i -= 1

        return steps