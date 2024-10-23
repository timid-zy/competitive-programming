from math import factorial as f

MOD = 998244353
def solve():
    S = input()
    res = curr = 1
    changes = 0
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            curr += 1
            changes += 1
        else:
            res = (res * curr) % MOD
            curr = 1
    
    res = (res * curr * f(changes)) % MOD
    return changes, res

for _ in range(int(input())):
    res = solve()
    print(*res)