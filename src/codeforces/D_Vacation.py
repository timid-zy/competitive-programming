def solve():
    N = int(input())
    di = input()

    BC = [[1, 1] for _ in range(N+1)]
    for i in range(1, len(BC)):
        dire = di[i-1]
        if dire == "L":
            BC[i][0] = BC[i-1][1] + 1
        else:
            BC[i][1] = BC[i-1][0] + 1
    
    FC = [[1, 1] for _ in range(N+1)]
    for i in range(len(FC) - 2, -1, -1):
        dire = di[i]
        if dire == "R":
            FC[i][0] = FC[i+1][1] + 1
        else:
            FC[i][1] = FC[i+1][0] + 1

    return [(BC[i][0] + FC[i][0] - 1) for i in range(N+1)]

for _ in range(int(input())):
    ans = solve()
    print(*ans)
