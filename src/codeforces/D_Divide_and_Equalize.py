from collections import defaultdict

sieve = [0] * (10 ** 6 + 2)
primes = []
for i in range(2, 10 ** 6 + 2):
    if sieve[i] == 0:
        primes.append(i)
        for j in range(i*i, 10 ** 6 + 2, i):
            sieve[j] = 1

def add_factors(x, counter):
    i = 0
    while x > 1:
        if x % primes[i] == 0:
            counter[primes[i]] += 1
            x //= primes[i]
        else:
            i += 1


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    counter = defaultdict(int)
    for n in A:
        if n == 1:
            continue

        if sieve[n] == 0:
            counter[n] += 1
            continue

        add_factors(n, counter)
    
    return all(v % N == 0 for k, v in counter.items())


for _ in range(int(input())):
    ans = "YES" if solve() else "NO"
    print(ans)