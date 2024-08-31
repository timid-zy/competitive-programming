def solve(N, X, M):
    main = [float('inf'), float('-inf')]
    for _ in range(M):
        l, r = list(map(int, input().split()))
        if (main[0] <= l <= main[1]) or (main[0] <= r <= main[1]) or (l <= X <= r):
            main[0] = min(main[0], l)
            main[1] = max(main[1], r)
    
    return main


for _ in range(int(input())):
    N, X, M = map(int, input().split())
    main = solve(N, X, M)
    print(max(main[1] - main[0] + 1, 1))