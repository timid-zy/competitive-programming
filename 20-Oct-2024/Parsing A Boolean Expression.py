class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c == "(" or c == ",":
                continue

            if c in "!|&":
                stk.append(c)
                continue
            
            if c == ")":
                if stk[-2] in "|&":
                    stk[-2] = stk[-1]
                    stk.pop()
                else:
                    stk[-2] = not stk[-1]
                    stk.pop()
                
                op = ""
                sti = 0
                for i in range(len(stk) - 1, -1, -1):
                    if type(stk[i]) != bool:
                        op = stk[i]
                        sti = i+1
                        break
                
                while sti + 1 < len(stk):
                    if op == "&":
                        stk[sti] &= stk[-1]
                        stk.pop()
                    else:
                        stk[sti] |= stk[-1]
                        stk.pop()

                continue
            
            b = True if c == "t" else False
            if stk[-1] == str(stk[-1]) and stk[-1] in "!|&":
                stk.append(b)
                continue

            if stk[-2] == "&":
                stk[-1] &= b
            elif stk[-2] == "|":
                stk[-1] |= b
        
        return stk[0]