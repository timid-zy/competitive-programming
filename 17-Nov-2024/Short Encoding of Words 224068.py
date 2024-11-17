# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def add(word, root):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c] 
            
            curr.is_end = True

        root = TrieNode()
        for w in words:
            add(reversed(w), root)
        
        stk = [(root, 0)]
        res = 0
        while stk:
            cn, cd = stk.pop()
            if len(cn.children) == 0:
                res += cd + 1

            for nb in cn.children:
                stk.append((cn.children[nb], cd+1))
        
        return res
