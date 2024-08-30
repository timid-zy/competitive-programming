n = int(input())
A = list(map(int, input().split()))

res = [0] * n
res[-1] = A[-1]
r_sum = res[-1] if n % 2 == 0 else -res[-1]
for i in range(n-2, -1, -1):
    if i % 2 == 1:
        res[i] = A[i] - r_sum
        r_sum += res[i]
    else:
        res[i] = A[i] + r_sum
        r_sum -= res[i]

print(*res)