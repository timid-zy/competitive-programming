class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        def rec(o, c, curr=""):
            nonlocal arr
            if o == 0 and c == 0:
                arr.append(curr)
                return
            
            if o > 0:
                rec(o - 1, c, curr + "(")
            if c > 0 and c > o:
                rec(o, c - 1, curr + ")")

        rec(n, n)
        return arr