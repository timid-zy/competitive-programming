from collections import Counter

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def checkCycle(s):
    ss = s + s
    for i in range(1, len(s)):
        if s == ss[i: i + len(s)]:
            return i
    
    return len(s)


for _ in range(int(input())):
    n = int(input())
    s = input()
    arr = list(map(int, input().split()))

    res = []
    for i in range(len(arr)):
        curr = i
        c = ""

        while arr[curr] != -1:
            c += s[curr]
            old = curr
            curr = arr[curr] - 1
            arr[old] = -1
        
        if not c:
            continue
    
        res.append(checkCycle(c))
    
    lcm = 1
    for i in range(len(res)):
        lcm = (lcm * res[i]) // gcd(lcm, res[i])
    
    print(lcm)