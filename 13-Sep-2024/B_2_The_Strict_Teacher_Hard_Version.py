from math import ceil

def solve():
    N, M, Q = list(map(int, input().split()))
    teachers = list(set(map(int, input().split())))
    queries = list(map(int, input().split()))

    spts = set(teachers)
    teachers.sort()
    queries = list(zip(queries, range(len(queries))))
    queries.sort()
    q = 0
    res = []
    while q < len(queries) and queries[q][0] <= teachers[0]:
        if queries[q][0] in spts:
            res.append(0)
            q += 1
            continue
        
        res.append(teachers[0] - 1)
        q += 1

    t1, t2 = 0, 1
    while q < len(queries) and t2 < len(teachers):
        if queries[q][0] in spts:
            q += 1
            res.append(0)
            continue
            
        if queries[q][0] > teachers[-1]:
            break

        res.append(ceil((teachers[t2] - teachers[t1] - 1) / 2))
        q += 1
        while q < len(queries) and t2 < len(teachers) and queries[q][0] > teachers[t2]:
            t1 += 1
            t2 += 1
    
    while q < len(queries):
        if queries[q][0] in spts:
            res.append(0)
            q += 1
            continue
    
        res.append(N - teachers[-1])
        q += 1
    
    ans = [0] * len(queries)
    for i in range(len(res)):
        ans[queries[i][1]] = res[i]

    return ans


for _ in range(int(input())):
    ans = solve()
    for t in ans:
        print(t)
