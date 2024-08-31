class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        _dict = {}
        for i in range(len(s)):
            _dict[s[i]] = i
        
        arr = []
        limit = _dict[s[0]]
        start = 0

        for i in range(len(s)):
            char = s[i]
            limit = max(limit, _dict[char])
            if limit == i:
                arr.append(limit - start + 1)
                start = limit + 1
                if start < len(s):
                    limit = _dict[s[start]]
            
        return arr