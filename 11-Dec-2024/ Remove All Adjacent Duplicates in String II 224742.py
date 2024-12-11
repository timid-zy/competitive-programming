# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for i in range(len(s)):
            if len(stk) == 0 or stk[-1][0] != s[i]:
                stk.append([s[i], 1])
            else:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
        
        return "".join([c * ci for c, ci in stk])