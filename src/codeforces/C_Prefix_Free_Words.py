from collections import deque

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None, None]


def search(n):
    stack = [(root, 0)]
    path = {root: None}
    last = None
    while stack:
        node, curr = stack.pop()
        if curr == n:
            node.end = True
            last = node
            break
        
        if curr > n:
            continue

        if node.children[0] is None:
            node.children[0] = TrieNode()
        if node.children[1] is None:
            node.children[1] = TrieNode()

        if not node.children[0].end:
            stack.append((node.children[0], curr + 1))
            path[node.children[0]] = node
        
        if not node.children[1].end:
            stack.append((node.children[1], curr + 1))
            path[node.children[1]] = node
        
        if node.children[0].end and node.children[1].end:
            node.end = True
        
    if last is None: return None

    s = []
    while path[last] is not None:
        p = path[last]
        if last == p.children[0]:
            s.append("0")
        else:
            s.append("1")
        
        last = p
    
    return "".join(s[::-1])

    
root = TrieNode()  
def solve():
    input()
    A = list(map(int, input().split()))
    arr = sorted(list(zip(A, range(len(A)))), key=lambda x: x[0])
    ans = [None] * len(arr)

    for n, idx in arr:
        w = search(n)
        if w is None:
            print("NO")
            return
        ans[idx] = w
    
    print("YES")
    for w in ans:
        print(w)
        
solve()