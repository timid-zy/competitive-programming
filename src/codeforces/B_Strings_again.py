from collections import Counter

def solve():
    n, m, k = map(int, input().split())
    a = Counter(input())
    b = Counter(input())

    A, B = [], []
    for c in sorted(a.keys()):
        A.append([c, a[c]])
    
    for c in sorted(b.keys()):
        B.append([c, b[c]])
    
    curr = ""
    limit = 0
    i = j = 0
    res = []
    while i < len(A) and j < len(B):
        if (A[i][0] < B[j][0] or (limit == k and curr == "B")) and not (limit == k and curr == "A"):
            if curr == "A":
                limit += 1
            else:
                limit = 1
                curr = "A"
            res.append(A[i][0])
            A[i][1] -= 1
            if A[i][1] == 0:
                i += 1
        
        else:
            if curr == "B":
                limit += 1
            else:
                limit = 1
                curr = "B"
            
            res.append(B[j][0])
            B[j][1] -= 1
            if B[j][1] == 0:
                j += 1

    print("".join(res))


for _ in range(int(input())):
    solve()