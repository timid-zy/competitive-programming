from math import ceil

def solve():
    N, M, Q = map(int, input().split())
    S, E = sorted(list(map(int, input().split())))
    D = int(input())

    if S == D or E == D:
        return 0
    elif S < D < E:
        return ceil((E - S - 1) / 2)
    elif D < S:
        return S - 1
    elif E < D:
        return N - E

for _ in range(int(input())):
    print(solve())
