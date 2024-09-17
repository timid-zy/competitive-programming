class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter()
        for a in s1.split(" "):
            counter[a] += 1
        
        for b in s2.split(" "):
            counter[b] += 1

        res = []
        for k in counter:
            if counter[k] == 1:
                res.append(k)
        
        return res
    