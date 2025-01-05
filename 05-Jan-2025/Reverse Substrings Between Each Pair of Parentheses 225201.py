# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for i, c in enumerate(s):
            if c != ")":
                stk.append(c)
                continue
            
            stk2 = []
            while stk[-1] != "(":
                stk2.append(stk.pop())
            
            stk.pop()
            stk.extend(stk2)

        return "".join(stk)