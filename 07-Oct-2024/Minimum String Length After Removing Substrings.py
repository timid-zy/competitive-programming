class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and c == "B" and stk[-1] == "A":
                stk.pop()
            elif stk and c == "D" and stk[-1] == "C":
                stk.pop()
            else:
                stk.append(c)
        
        return len(stk)
