N, M = map(int, input().split())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

i = j = 0
res = []
while i < len(A1) and j < len(A2):
    if A1[i] <= A2[j]:
        res.append(A1[i])
        i += 1
    else:
        res.append(A2[j])
        j += 1

res.extend(A1[i:])
res.extend(A2[j:])

print(*res)