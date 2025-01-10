class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = defaultdict(int)
        for w in words2:
            c2 = Counter(w)
            for k in c2:
                count[k] = max(count[k], c2[k])
            
        res = []
        for w in words1:
            c1 = Counter(w)
            valid = True
            for k in count:
                if count[k] > c1[k]:
                    valid = False
                    break
            
            if valid:
                res.append(w)
        
        return res
    
