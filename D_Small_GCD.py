def getFactors(n):
    a = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            a.append(d)
        
        d += 1
    
    for i in range(len(a) - 1, -1, -1):
        a.append(n // a[i])
    
    return a

def findMaxIdx(d, x):
    for i in range(len(d) - 1, -1, -1):
        if x % d[i] == 0:
            return d[i]


for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    arr.sort()
    divisors = []
    for j in range(len(arr)):
        divisors.append(getFactors(arr[j]))
    
    count = 0
    for j in range(1, len(arr) - 1):
        d = divisors[j]
        for k in range(j):
            gcd = findMaxIdx(d, arr[k])
            # print(arr[k], arr[j], gcd, gcd * (len(arr) - j - 1))
            count += (gcd) * (len(arr) - j - 1)
    
    print(count)