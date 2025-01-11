# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        total = l = 0
        rl, rr = 0, len(s)
        count = defaultdict(int)
        target = Counter(t)
        for i in range(len(s)):
            while total == len(t):
                if rr-rl > i-l:
                    rl, rr = l, i

                count[s[l]] -= 1
                if count[s[l]] < target[s[l]]:
                    total -= 1

                l += 1

            count[s[i]] += 1
            if count[s[i]] <= target[s[i]]:
                total += 1

        while total == len(t):
            if rr-rl > i-l:
                rl, rr = l, i + 1

            count[s[l]] -= 1
            if count[s[l]] < target[s[l]]:
                total -= 1

            l += 1
            
        res = Counter(s[rl:rr])
        for c in t:
            if res[c] < target[c]:
                return ""
        
        return s[rl:rr]
