from collections import deque

def solve():
    N, K = map(int, input().split())
    S = list(input())
    d = {"0": 0, "1": 1}
    qs = deque()
    count = [0, 0] # 0, 1
    for i in range(K):
        if S[i] == "?":
            qs.append(i)
            continue

        count[d[S[i]]] += 1
    
    if abs(count[0] - count[1]) - len(qs) > 0:
        return "NO"
    
    for _ in range(abs(count[0] - count[1])):
        qs.popleft()
        if count[0] < count[1]:
            count[0] += 1
        else:
            count[1] += 1
    
    for i in range(1, len(S) - K + 1):
        while qs and qs[0] < i:
            qs.popleft()
        
        r = i + K - 1
        if S[i-1] == "0":
            count[0] -= 1
        elif S[i-1] == "1":
            count[1] -= 1
        
        if S[r] == "0":
            count[0] += 1
        elif S[r] == "1":
            count[1] += 1
        else:
            qs.append(r)
        
        if abs(count[0] - count[1]) - len(qs) > 0:
            return "NO"

        for _ in range(abs(count[0] - count[1])):
            qs.popleft()
            if count[0] < count[1]:
                count[0] += 1
            else:
                count[1] += 1
    
    return "YES"

for _ in range(int(input())):
    print(solve())