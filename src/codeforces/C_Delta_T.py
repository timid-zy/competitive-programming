def solve():
    L, R, X = map(int, input().split())
    A, B = map(int, input().split())

    if A == B:
        return 0
    
    if abs(B-A) >= X:
        return 1

    if (abs(A-L) >= X and abs(B-L) >= X) or (abs(R-A) >= X and abs(R-B) >= X):
        return 2

    # L R L
    if abs(L-A) >= X and abs(R-L) >= X and abs(R-B) >= X:
        return 3
    
    # R L R
    if abs(R-A) >= X and abs(R-L) >= X and abs(B-L) >= X: 
        return 3
    
    return -1

for _ in range(int(input())):
    print(solve())