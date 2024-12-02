class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for idx, w in enumerate(words):
            valid = True
            for i in range(len(searchWord)):
                if i >= len(w):
                    valid = False
                    break
                
                if w[i] != searchWord[i]:
                    valid = False
                    break
            
            if valid:
                return idx + 1
        
        return -1