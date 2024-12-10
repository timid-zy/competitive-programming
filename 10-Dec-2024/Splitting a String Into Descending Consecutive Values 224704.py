# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        def checkString(currArr, currStr):
            if currStr == "" or (len(currArr) > 0 and currArr[-1] == int(currStr) + 1):
                return True
            
            for i in range(1, len(currStr)):
                if not currArr or (currArr[-1] == int(currStr[:i]) + 1) :
                    res = checkString(
                        currArr + [int(currStr[:i])],
                        currStr[i:]
                    )
                    if res: return True
            return False
        
        
        return checkString([], s)