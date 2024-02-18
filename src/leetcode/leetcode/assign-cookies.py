class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sortedG = sorted(g)
        sortedS = sorted(s)
        num = 0
        i = 0
        j = 0
        for i in range(len(s)):
            if j > len(g) - 1: break
            if sortedS[i] >= sortedG[j]:
                num += 1
                j += 1
        
        return num