class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces.sort()
        l = 0
        for i, c in enumerate(s):
            if l < len(spaces) and spaces[l] == i:
                res.append(" ")
                l += 1
            
            res.append(c)
        
        return "".join(res)