# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def add(word, root):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c]
            
            curr.is_end = True
        

        def find_longest(root):
            stk = [(root, "")]
            res = ""
            while stk:
                node, word = stk.pop()
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
                
                for k, nb in node.children.items():
                    if nb.is_end:
                        stk.append((nb, word + k))
            
            return res
            

        root = TrieNode()
        for word in words:
            add(word, root)
    
        return find_longest(root)