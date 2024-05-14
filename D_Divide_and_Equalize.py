from collections import Counter
import bisect

# generate primes
sieve = [0] * ((10 ** 6) + 1)
primes = []

for i in range(2, 10 ** 6):
    if sieve[i] == 0:
        primes.append(i)
    
        for j in range(i * i, 10 ** 6, i):
            sieve[j] = 1


def getPrimeFactorization(counter, n):
    global primes
    idx = 0
    while n != 1:
        d = primes[idx]
        if n % d == 0:
            counter[d] = counter.get(d, 0) + 1
            n //= d
            continue
        
        idx += 1
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    counter = Counter()
    
    for i in range(len(arr)):
        if arr[i] == 1:
            continue

        if sieve[arr[i]] == 0:
            counter[arr[i]] = counter.get(arr[i], 0) + 1
        else:
            getPrimeFactorization(counter, arr[i])

    flag = True
    for key in counter:
        if counter[key] % n != 0:
            flag = False
            break
    
    if flag:
        print('YES')
    else:
        print('NO')