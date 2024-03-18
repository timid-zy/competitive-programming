class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        left = 0 if s[0] == "|" else None
        for i in range(1, len(s)):
            if s[i] == "|":
                prefix.append(prefix[-1])
                left = i
            else:
                prefix.append(prefix[-1] + 1)
                if left is None: prefix[-1] -= 1

        bars = []
        for i in range(len(s)):
            if s[i] == "|":
                bars.append(i)
        
        res = []
        for start, end in queries:
            l = bisect_left(bars, start)
            r = bisect_right(bars, end) - 1
            if l >= len(bars) or r >= len(bars) or bars[l] > end or bars[r] < start: res.append(0)
            else: res.append(prefix[bars[r]] - prefix[bars[l]])
    
        return res