class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.count("L") != result.count("L") or start.count("R") != result.count("R"):
            return False
        
        ri = 0
        for si in range(len(start)):
            while ri < len(result) and result[ri] == "X":
                ri += 1
            
            if ri == len(result): return True
            if start[si] == "X": continue
            
            if (result[ri] == "L" and si < ri) or (result[ri] == "R" and si > ri) or result[ri] != start[si]:
                return False
            
            if result[ri] == start[si]:
                ri += 1
        
        return True