def solve():    
    _, M = map(int, input().split())
    A = list(map(int, input().split()))

    stk = [0]
    while stk:
        curr = stk.pop()
        if curr == M-1:
            return "YES"

        if curr >= len(A):
            break

        stk.append(curr + A[curr])
    
    return "NO"

print(solve())