def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    if s % 2 == 0:
        return 0
    
    res = float('inf')
    for n in arr:
        if n % 2 == 1:
            c = 0
            while n % 2 == 1:
                n //= 2
                c += 1
            
            res = min(c, res)
        
        else:
            c = 0
            while n > 0 and n % 2 == 0:
                n //= 2
                c += 1
            
            if n > 0: res = min(c, res)
    
    return res

for _ in range(int(input())):
    print(solve())