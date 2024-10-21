# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = r = 0
        while r < len(typed):
            if l < len(name) and name[l] == typed[r]:
                l += 1
            
            elif l == 0 and name[l] != typed[r]:
                return False
            
            elif typed[r] != name[l-1]:
                return False
            
            r += 1
        
        return l == len(name)
