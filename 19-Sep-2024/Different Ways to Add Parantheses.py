class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(s):
            if "+" not in s and "-" not in s and "*" not in s:
                return [int(s)]
            
            res = []
            for i in range(len(s)):
                if s[i] in ["+", "-", "*"]:
                    left = dfs(s[:i])
                    right = dfs(s[i+1:])
                    for l in left:
                        for r in right:
                            if s[i] == "+":
                                res.append(l+r)
                            elif s[i] == "-":
                                res.append(l-r)
                            else:
                                res.append(l*r)
            
            return res

        return dfs(expression)
