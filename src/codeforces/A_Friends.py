def solve():
    A, B = int(input()), int(input())
    n = abs(A-B)
    if n <= 1:
        return n

    t = n // 2
    res = (t * (t+1)) // 2
    return 2*res if n % 2 == 0 else 2*res + t + 1

print(solve())