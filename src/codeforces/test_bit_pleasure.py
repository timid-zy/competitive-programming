class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


def insert(num):
    word = bin(num)[2:]
    word = "0" * (46 - len(word)) + word
    curr = root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        
        curr = curr.children[c]
    
    curr.end = True

def findComp(num):
    word = bin(num)[2:]
    word = "0" * (46 - len(word)) + word
    comp = ""
    for i in range(len(word) - 1, -1, -1):
        comp += "1" if word[i] == "0" else "0"
    
    curr = root
    res = ""
    for c in comp:
        if c not in curr.children:
            nc = "1" if c == "0" else "0"
            res += nc
            curr = curr.children[nc]
        else:
            res += c
            curr = curr.children[c]
    
    print(num, int(res, 2))
    return int(res, 2)

        

root = TrieNode() # PREFIXES
insert(32)
insert(5)
insert(6)
print(findComp(25))