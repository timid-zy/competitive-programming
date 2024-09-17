def get_mn(n, m):
    if m == 0 and n == 1:
        return 0
    
    if m > n * 9 or m == 0:
        return -1

    res = [0] * n
    res[0] += 1
    m -= 1
    i = n-1
    while m > 0:
        d = min(9, m)
        res[i] += d
        m -= d
        i -= 1
    
    return "".join(map(str, res))

def get_mx(n, m):
    if m == 0 and n == 1:
        return 0
    
    if m > n * 9 or m == 0:
        return -1

    res = [0] * n
    i = 0
    while m > 0:
        d = min(9, m)
        res[i] = d
        m -= d
        i += 1
    
    return "".join(map(str, res))


N, M = map(int, input().split())
print(get_mn(N, M), get_mx(N, M))