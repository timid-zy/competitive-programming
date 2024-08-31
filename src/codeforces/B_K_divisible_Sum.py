from math import ceil

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n > k:
        k *= ceil(n/k)

    print(ceil(k/n))
