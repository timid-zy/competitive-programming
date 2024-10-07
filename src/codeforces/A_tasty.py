N, M = map(int, input().split())
res = [N // M for _ in range(M)]
for i in range(N % M):
    res[i] += 1

print(*reversed(res))