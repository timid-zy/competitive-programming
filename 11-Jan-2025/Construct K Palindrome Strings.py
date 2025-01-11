class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = Counter(s)
        for r in count:
            count[r] %= 2
        
        return sum(count[r] for r in count) <= k