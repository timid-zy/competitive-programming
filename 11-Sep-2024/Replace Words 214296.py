# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def find(word, trie):
            parent = trie
            for i, c in enumerate(word):
                print(c, parent.children, parent.isend)
                if c not in parent.children:
                    return word

                parent = parent.children[c]
                if parent.isend:
                    return word[:i+1]
                
                
            
            return word
        
        def add(word, trie):
            parent = trie
            for i, c in enumerate(word):
                if c not in parent.children:
                    parent.children[c] = TrieNode()
                
                parent = parent.children[c]
            
            parent.isend = True

        root = TrieNode()
        for word in dictionary:
            add(word, root)

        res = []
        for word in sentence.split(" "):
            res.append(find(word, root))
    
        return " ".join(res)
