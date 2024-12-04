class Solution:
    def calculate(self, s: str) -> int:
        def solve(l, r, neg=False):
            if l > r or l >= len(s):
                return 0

            if s[l] == "(":
                p = 1
                for i in range(l+1, len(s)):
                    if s[i] == "(": p += 1
                    elif s[i] == ")": p -= 1
                    if p == 0:
                        bres = solve(l+1, i-1)
                        if neg:
                            bres *= -1

                        if i+1 < len(s):
                            return bres + solve(i+2, r) if s[i+1] == "+" else bres + solve(i+2, r, True)

                        return bres
            
            if s[l] == "-":
                return solve(l+1, r, True)
            
            t = ""
            while l < len(s) and s[l] in "0123456789":
                t += s[l]
                l += 1

            if l == len(s) or s[l] == ")":
                return int(t) if not neg else -int(t)
            elif s[l] == "+":
                return int(t) + solve(l+1, r) if not neg else -int(t) + solve(l+1, r)
            elif s[l] == "-":
                return int(t) + solve(l+1, r, True) if not neg else -int(t) + solve(l+1, r, True)
            

        s = s.replace(" ", "")
        return solve(0, len(s)-1)