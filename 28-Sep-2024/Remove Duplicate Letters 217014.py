# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stk = []
        for i in range(len(s)):
            if s[i] in stk:
                counter[s[i]] -= 1
                continue

            while stk and stk[-1] >= s[i] and counter[stk[-1]] > 0:
                stk.pop()
            
            counter[s[i]] -= 1
            stk.append(s[i])
        
        return "".join(stk)
