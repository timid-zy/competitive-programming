class Solution:
    def minSwaps(self, s: str) -> int:
        l = swaps = curr = 0
        r = len(s) - 1
        while l < r:
            if s[l] == "[":
                curr += 1
            else:
                curr -= 1
            
            if curr >= 0:
                l += 1
                continue
            
            swaps += 1
            while r > l and s[r] != "[":
                r -= 1
            

            curr += 2
            r -= 1
            l += 1
        
        return swaps