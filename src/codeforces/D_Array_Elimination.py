def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    bits = [0] * 33
    for n in arr:
        for i in range(33):
            if n & (1 << i):
                bits[i] += 1
    
    res = []
    for i in range(1, len(arr) + 1):
        valid = True
        for j in range(33): valid &= bits[j] % i == 0

        if valid:
            res.append(i)
    
    print(*res)

for _ in range(int(input())):
    solve()