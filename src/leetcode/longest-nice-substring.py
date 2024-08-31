class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def longestNice(s):
            nonlocal nicest
            if len(s) <= 1:
                return 
            
            count = dict(Counter(s))
            valid = True
            invalid_idx = -1
            for i in range(len(s)):
                if s[i].lower() not in count or s[i].upper() not in count:
                    valid = False
                    invalid_idx = i
                    break
            
            if valid:
                if len(s) > len(nicest):
                    nicest = s
                return 
            else:
                longestNice(s[:invalid_idx])
                longestNice(s[invalid_idx + 1:])

        nicest = ""
        longestNice(s)
        return nicest