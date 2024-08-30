for _ in range(int(input())):
    n = int(input())
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    
    while n % 3 == 0:
        n =  n // 3
        k += 2
    
    while n % 5 == 0:
        n = n // 5
        k += 3
    
    if n == 1:
        print(k)
    else:
        print(-1)