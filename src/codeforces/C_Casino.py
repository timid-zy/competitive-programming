import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def checkFactors(n):
    d = 2

    while n > 1:
        if d > 3:
            return False
        if n % d == 0:
            n //= d
        else:
            d += 1
    
    return True


input()
arr = list(map(int, input().split()))

gc = arr[0]
for i in range(1, len(arr)):
    gc = gcd(gc, arr[i])

valid = True
for i in range(len(arr)):
    ops = arr[i] // gc
    if not checkFactors(ops):
        valid = False
        break

if valid:
    print('Yes')
else:
    print('No')

# input()
# arr = list(map(int, input().split()))
# gc = arr[0]

# for i in range(1, len(arr)):
#     gc = gcd(gc, arr[i])

# lcm = arr[0]
# for i in range(1, len(arr)):
#     gc = gcd(lcm, arr[i])
#     lcm = lcm * arr[i] // gc

# valid = True
# if not checkFactors(lcm // gc):
#     print('No')
# else:
#     print('Yes')