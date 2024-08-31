input()
k, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

mvA = mvB = 0
for i in range(k):
    while mvB < len(B) and A[i] >= B[mvB]:
        mvB += 1


ans = "YES" if len(B) - mvB >= m else "NO"
print(ans)