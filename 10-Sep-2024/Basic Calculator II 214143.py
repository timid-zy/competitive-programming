# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        op = ["+", "-", "/", "*"]
        stk = [""]
        for c in s:
            if c == "":
                continue
            if c in op:
                stk[-1] = int(stk[-1])
                stk.append(c)
                stk.append("")
            else:
                stk[-1] += c
        
        stk[-1] = int(stk[-1])
        stk2, i = [], 0
        while i < len(stk):
            if stk[i] == "/":
                stk2[-1] //= stk[i+1]; i += 1
            elif stk[i] == "*":
                stk2[-1] *= stk[i+1]; i += 1
            else:
                stk2.append(stk[i])
            
            i += 1
        
        res = i = 0
        while i < len(stk2):
            if stk2[i] == "-":
                res -= stk2[i+1]; i += 1
            elif stk2[i] != "+":
                res += stk2[i]
            
            i += 1

        return res
