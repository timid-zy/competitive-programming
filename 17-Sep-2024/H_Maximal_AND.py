def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    pos = [0] * 31
    for n in A:
        for i in range(31):
            if n & (1 << i):
                pos[i] += 1
    
    res = 0
    for i in range(30, -1, -1):
        if pos[i] == N:
            res |= (1 << i)
        elif K >= 0 and pos[i] + K >= N:
            res |= (1 << i)
            K -= N - pos[i]
        
    
    return res

for _ in range(int(input())):
    print(solve())