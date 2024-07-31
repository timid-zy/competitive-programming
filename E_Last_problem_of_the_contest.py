def solve():
    input()
    A = list(map(int, input().split()))
    powers_of_two = set()
    n = 1
    while n <= 2 * 10 ** 9 + 2:
        powers_of_two.add(n)
        n *= 2

    setA = set(A)
    res = []
    for x in A:
        for c in powers_of_two:
            if (x - c) in setA and (x + c) in setA:
                return [x - c, x, x + c]
            
            if (x + c) in setA:
                res = [x + c, x]
            
            if (x - c) in setA:
                res = [x - c, x]
    
    if len(res) > 1:
        return res

    return [A[0]]

ans = solve()
print(len(ans))
print(*ans)