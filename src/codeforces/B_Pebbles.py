import math

def get_largest_divisor(x):
    for i in range(2, math.ceil(x ** 0.5) + 1):
        if x % i == 0:
            return x // i
    
    return 1
    
peb = res = int(input())
while peb > 1:
    peb = get_largest_divisor(peb)
    res += peb

print(res)