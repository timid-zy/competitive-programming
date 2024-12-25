# Problem: Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            
            if stk[-1][1] == k:
                stk.pop()
        
        res = ""
        for c, count in stk:
            res += c * count
        
        return res