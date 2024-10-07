class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        self.count = 0


def insert(word):
    curr = root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        
        curr = curr.children[c]
        curr.count += 1

def count(word):
    res = TOTAL + len(words)*len(word)
    deduct = 0
    curr = root
    for c in reversed(word):
        if c not in curr.children:
            break

        deduct += curr.count
        curr = curr.children[c]
    
    deduct += curr.count
    return res - (deduct * 2)

N = int(input())
root = TrieNode()
words = []
TOTAL = 0

for _ in range(N):
    w_in = input()
    words.append(w_in)
    TOTAL += len(w_in)
    insert(w_in)

ans = 0
for w in words:
    ans += count(w)

print(ans)
