def solve():
    N, K = map(int, input().split())
    if N == 1 and K == 1:
        print(1)
        print(1)
        return

    if K == 1 or N == K:
        print(-1)
        return
    
    is_odd = (K-1) % 2 == 1
    if is_odd:
        print(3)
        print(1, K, K+1)
        return

    print(5)
    print(1, 2, K, K+1, K+2)

for _ in range(int(input())):
    solve()