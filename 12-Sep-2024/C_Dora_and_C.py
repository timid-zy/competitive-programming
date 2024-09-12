def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def solve():
    N, A, B = map(int, input().split())
    ARR = list(map(int, input().split()))
    rems = []
    gc = gcd(A, B)
    for n in ARR: rems.append(n % gc)

    rems.sort()
    ans = rems[-1] - rems[0]
    for i in range(1, len(rems)):
        ans = min(ans, (rems[i-1] + gc) - rems[i])
    
    return ans

for _ in range(int(input())):
    print(solve())