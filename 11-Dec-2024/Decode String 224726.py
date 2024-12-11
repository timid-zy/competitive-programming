# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def rec(l, r):
            if l > r:
                return ""
            
            if ord('a') <= ord(s[l]) <= ord('z'):
                return s[l] + rec(l+1, r)
            
            rn = l
            while rn <= r and s[rn] != "[":
                rn += 1
            
            rep = int(s[l:rn])
            rb = rn+1
            lvl = 1
            while lvl > 0:
                if s[rb] == "[":
                    lvl += 1
                
                if s[rb] == "]":
                    lvl -= 1
                
                rb += 1
            
            return rep * rec(rn+1, rb-2) + rec(rb, r)
        
        return rec(0, len(s) - 1)