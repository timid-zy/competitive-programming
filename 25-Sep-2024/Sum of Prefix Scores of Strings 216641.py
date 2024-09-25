# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class TrieNode():
            def __init__(self):
                self.children = {}
                self.is_end = False
                self.count = 0
            
        def add(word, root):
            parent = root
            for c in word:
                if c not in parent.children:
                    parent.children[c] = TrieNode()
                
                parent = parent.children[c]
                parent.count += 1
            
            parent.is_end = True
        
        def get_score(word, root):
            res = 0
            parent = root
            for c in word:
                parent = parent.children[c]
                res += parent.count
            
            return res
        
        root = TrieNode()
        for w in words:
            add(w, root)
        
        res = []
        for w in words:
            res.append(get_score(w, root))
        
        return res
