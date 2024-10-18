from math import factorial as f

MOD = 998244353
def solve():
    S = input()
    
    consec = 0
    res1 = 0
    cmb = 1
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            consec += 1
            res1 += 1
        else:
            cmb = (cmb * (consec + 1)) % MOD
            consec = 0
    
    if consec >= 1:
        cmb = (cmb * (consec + 1)) % MOD
    
    cmb = (cmb * f(res1) % MOD) % MOD
    return [res1, cmb]

for _ in range(int(input())):
    ans = solve()
    print(*ans)

