# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

for _ in range(int(input())):
    N = int(input())
    mat = []
    for __ in range(N):
        mat.append(list(map(int, input().split())))
    
    if N == 1:
        print("YES")
        print(1)
        continue

    res = [None] * N
    for r in range(N):
        for c in range(N):
            if r != c:
                if res[r] is None: res[r] = mat[r][c]
                else: res[r] &= mat[r][c]

                if res[c] is None: res[c] = mat[r][c]
                else: res[c] &= mat[r][c]
    
    valid = True
    for r in range(N):
        for c in range(N):
            if r != c and mat[r][c] != res[r] | res[c]:
                valid = False
                break
        
        if not valid: break

    if valid:
        print("YES")
        print(*res)
    else:
        print("NO")
