MOD = 10 ** 9 + 7

def mod_inverse(a, m):
    return pow(a, m-2, m)

def solve():
    N, m = map(int, input().split())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    eq2 = m * (m-1) // 2
    tz = s1.count(0) + s2.count(0)
    Q = pow(m, tz, MOD)

    zeroes = [0] * N
    for i in range(len(zeroes) - 2, -1, -1):
        zeroes[i] = zeroes[i+1]
        if s1[i+1] == 0:
            zeroes[i] += 1
        if s2[i+1] == 0:
            zeroes[i] += 1

    p = 0
    equals = 1
    for i in range(len(s1)):
        t = 0
        if s1[i] == 0 and s2[i] == 0:
            t = (equals * eq2) % MOD
            equals = (equals * m) % MOD
        
        elif s1[i] == 0:
            t = (equals * (m-s2[i])) % MOD
        
        elif s2[i] == 0:
            t = (equals * (s1[i] - 1)) % MOD
        
        else:
            d = s1[i] - s2[i]
            if d < 0:
                break
            
            if d > 0:
                t = (equals * max(1, pow(m, zeroes[i], MOD))) % MOD
                p = (p + t) % MOD
                break

            if d == 0:
                continue
        
        t = (t * pow(m, zeroes[i], MOD)) % MOD
        p = (p + t) % MOD
    # print(p, Q)
    return (p * mod_inverse(Q, MOD)) % MOD


print(solve())