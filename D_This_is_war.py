def solve():
    input()
    A = list(map(int, input().split()))
    A = list(zip(A, range(len(A))))
    A.sort()
    prev = 0
    can_win = [False] * len(A)
    r_sum = 0
    for i in range(len(A) - 1):
        r_sum += A[i][0]
        if r_sum < A[i+1][0]:
            prev = i+1
    
    res = []
    for j in range(prev, len(A)):
        res.append(A[j][1] + 1)
            
    res.sort()
    return res

for _ in range(int(input())):
    ans = solve()
    print(len(ans))
    print(*ans)