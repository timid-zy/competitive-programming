class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


def insert(word):
    curr = root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        
        curr = curr.children[c]
    
    curr.end = True

root = TrieNode()