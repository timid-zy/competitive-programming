# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(i, p1, p2, c=0):
            if i == len(num):
                return c >= 3
            
            if num[i] == "0":
                if p1 is None or p2 is None or p1 + p2 == 0:
                    return backtrack(i+1, p2, 0, c + 1)
                
                return False
            
            for j in range(i+1, len(num) + 1):
                if p1 is None or p2 is None or p1 + p2 == int(num[i:j]):
                    if backtrack(j, p2, int(num[i:j]), c + 1):
                        return True
            
            return False
        
        return backtrack(0, None, None)
            