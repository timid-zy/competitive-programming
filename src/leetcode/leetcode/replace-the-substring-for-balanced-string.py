class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        req = Counter({'Q': n, 'W': n, 'E': n, 'R': n})
        req = dict(Counter(s) - req)
        if len(req) == 0: return 0
        print(req)
        
        curr = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        start = 0
        min_len = len(s)
        for i in range(len(s)):
            if s[i] not in req: continue
            
            curr[s[i]] += 1
            while start < len(s) and (s[start] not in req or curr[s[start]] > req[s[start]]):
                curr[s[start]] -= 1
                start += 1
            
            valid = True
            for key in req:
                if curr[key] < req[key]:
                    valid = False
                    break
            if valid: 
                min_len = min(min_len, i - start + 1)

        return min_len