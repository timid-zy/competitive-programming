from math import ceil

def solve():
    N, K = map(int, input().split())
    if K >= N:
        return 1
    
    ans = N
    for i in range(2, ceil(N ** 0.5) + 1):
        if N % i == 0 and N // i <= K:
            ans = min(ans, i)

        if N % i == 0 and i <= K:
            ans = min(ans, N // i)

    return ans

for _ in range(int(input())):
    print(solve())