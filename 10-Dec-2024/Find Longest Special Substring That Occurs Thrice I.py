class Solution:
    def maximumLength(self, s: str) -> int:
        def check_window_size(k):
            count = defaultdict(int)
            curr = defaultdict(int)
            l = 0
            for i in range(k):
                curr[s[i]] += 1
            
            if len(curr) == 1:
                count[s[:k]] += 1

            for r in range(k, len(s)):
                curr[s[r]] += 1
                curr[s[l]] -= 1
                if curr[s[l]] == 0:
                    del curr[s[l]]
                
                l += 1
                if len(curr) == 1:
                    count[s[l:r+1]] += 1

            return any(v >= 3 for v in count.values())
        
        l, r = 1, len(s) - 2
        while l < r:
            mid = (r + l + 1) // 2
            if check_window_size(mid):
                l = mid
            else:
                r = mid-1
            
        return l if check_window_size(l) else -1