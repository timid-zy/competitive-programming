def checkPowerOfTwo(n):
    while n > 1:
        if n % 2 == 0:
            n //= 2
        
        else:
            return False
    
    return True

for i in range(int(input())):
    n = int(input())
    
    if checkPowerOfTwo(n):
        print('NO')
    else:
        print('YES')