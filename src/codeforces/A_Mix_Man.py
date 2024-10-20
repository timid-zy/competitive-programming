def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(len(A)):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
    
    return max(A) * max(B)

for _ in range(int(input())):
    print(solve())