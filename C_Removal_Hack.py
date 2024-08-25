from collections import defaultdict

N = int(input())
children = defaultdict(list)
cVals = {}
for i in range(1, N+1):
    p, c = map(int, input().split())
    if p == -1:
        cVals[i] = 0
        continue

    cVals[i] = c
    children[p].append(i)

res = []
for i in range(1, N+1):
    valid = cVals[i] == 1
    for child in children[i]:
        valid &= (child not in cVals or cVals[child] == 1)

    if valid:
        res.append(i)

ans = sorted(res) if res else [-1]
print(*ans)
