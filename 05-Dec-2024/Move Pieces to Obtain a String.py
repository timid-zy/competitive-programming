class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.count("L") != target.count("L") or start.count("R") != target.count("R"):
            return False
        
        ti = 0
        for si in range(len(start)):
            while ti < len(target) and target[ti] == "_":
                ti += 1
            
            if ti == len(target):
                return True
            
            if start[si] == "_":
                continue
            
            if (target[ti] == "L" and si < ti) or (target[ti] == "R" and si > ti) or (target[ti] != start[si]):
                return False
            
            if start[si] == target[ti]:
                ti += 1
        
        return True