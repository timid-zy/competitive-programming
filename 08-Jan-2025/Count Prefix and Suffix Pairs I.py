class Solution:
    def isPS(self, w1, w2):
        if len(w2) < len(w1):
            return False

        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return False
        
        j = len(w2)-1
        for i in range(len(w1)-1, -1, -1):
            if w1[i] != w2[j]:
                return False
            
            j -= 1
        
        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPS(words[i], words[j]):
                    res += 1
            
        return res