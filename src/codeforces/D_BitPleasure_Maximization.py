class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

def insert(num):
    curr = root
    for i in range(45, -1, -1):
        c = min(num & (1 << i), 1)
        if c not in curr.children:
            curr.children[c] = TrieNode()
        
        curr = curr.children[c]
    
    curr.end = True

def findComp(num):
    comp = ~num
    curr = root
    res = 0
    for i in range(45, -1, -1):
        c = min((1 << i) & comp, 1)
        if c not in curr.children:
            nc = 1 if c == 0 else 0
            res |= (nc << i)
            curr = curr.children[nc]
        else:
            res |= (c << i)
            curr = curr.children[c]
    
    return res


root = TrieNode() # PREFIXES
N = int(input())
arr = list(map(int, input().split()))
prefix = [0] * len(arr)
prefix[0] = arr[0]
postfix = [0] * len(arr)
postfix[-1] = arr[-1]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] ^ arr[i]

for i in range(len(arr) - 2, -1, -1):
    postfix[i] = postfix[i+1] ^ arr[i]

ans = max(max(prefix), max(postfix), 0)
insert(0)
for i in range(1, len(postfix)):
    insert(prefix[i-1])
    ans = max(ans, findComp(postfix[i]) ^ postfix[i])

ans = max(ans, findComp(0))
print(ans)
