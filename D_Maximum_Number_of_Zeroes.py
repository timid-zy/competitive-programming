from collections import defaultdict
input()
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

counter = defaultdict(int)
external = 0
for i in range(len(a1)):
    if a1[i] == 0:
        if a2[i] == 0:
            external += 1
        continue

    elif a2[i] == 0:
        counter[(0,0)] += 1
        continue
    
    a, b = a1[i], a2[i]
    if b < 0:
        a *= -1
        b *= -1

    gc = gcd(abs(a), abs(b))
    d = (a // gc, b // gc)
    counter[d] += 1

if len(counter) > 0:
    print(max(counter.values()) + external)
else:
    print(external)