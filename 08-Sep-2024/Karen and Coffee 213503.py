# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

N, K, M = map(int, input().split())
Q = [0] * (2 * (10 ** 5) + 1)

for _ in range(N):
    a, b = map(int, input().split())
    Q[a-1] -= 1
    Q[b] += 1

r_sum = 0
for i in range(len(Q) - 1, -1, -1):
    r_sum += Q[i]
    Q[i] = r_sum

admissable = [0] * len(Q)
r_sum = 0
for i in range(len(Q)):
    if Q[i] >= K:
        r_sum += 1
    
    admissable[i] = r_sum

for _ in range(M):
    a, b = map(int, input().split())
    print(admissable[b] - admissable[a-1])
