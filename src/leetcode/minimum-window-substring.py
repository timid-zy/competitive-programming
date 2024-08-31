class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        req = dict(Counter(t))
        curr = {}
        for key in req: curr[key] = 0
        start = 0
        min_len = s + " "
        for end in range(len(s)):
            if s[end] not in req: continue
            curr[s[end]] += 1
            while start < len(s) and (s[start] not in req or curr[s[start]] > req[s[start]]):
                if s[start] in curr:
                    curr[s[start]] -= 1
                start += 1
            
            valid = True
            for key in req:
                if curr[key] < req[key]:
                    valid = False
                    break
            if valid:
                candidate = s[start: end + 1]
                min_len = candidate if len(candidate) < len(min_len) else min_len
        
        return min_len if len(min_len) != len(s) + 1 else ""