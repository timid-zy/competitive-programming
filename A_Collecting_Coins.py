for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    mx = max(a, b, c)
    n -= 3*mx - a - b - c

    if n >= 0 and n % 3 == 0:
        print('YES')
    else:
        print('NO')