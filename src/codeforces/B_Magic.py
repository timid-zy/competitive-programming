def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

for _ in range(int(input())):
    M = int(input())
    print(100 // gcd(100, M))
    