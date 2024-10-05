class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        t = Counter(s1)
        l = 0
        for r in range(len(s2)):
            if t[s2[r]] == 0:
                for k in t:
                    counter[k] = t[k]
                
                l = r + 1
                continue
            
            if counter[s2[r]] > 0:
                counter[s2[r]] -= 1
            else:
                while counter[s2[r]] == 0:
                    counter[s2[l]] += 1
                    l += 1
                
                counter[s2[r]] -= 1
            
            if r - l + 1 == len(s1):
                return True
        
        return False
    