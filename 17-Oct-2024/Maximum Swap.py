class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        counter = Counter(s)
        sarr = list(s)
        mx = max(sarr)
        l = 0
        while l < len(s) and s[l] == mx:
            counter[s[l]] -= 1
            if counter[s[l]] == 0 and len(counter) > 1:
                del counter[s[l]]
                mx = max(counter.keys())
            
            l += 1
        
        if l == len(s):
            return num
        
        for i in range(len(s) - 1, l, -1):
            if s[i] == mx:
                sarr[l], sarr[i] = sarr[i], sarr[l]
                break
            
        return int("".join(sarr))
