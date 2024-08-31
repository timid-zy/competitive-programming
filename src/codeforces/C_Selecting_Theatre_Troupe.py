from functools import cache

@cache
def factorial(x):
    if x <= 1: return 1
    return factorial(x-1) * x

n, m, t = map(int, input().split())
total = 0
for i in range(4, t):
    j = t - i
    total += (factorial(n) // (factorial(n-i) * factorial(i))) * (factorial(m) // (factorial(m-j) * factorial(j)))

print(total)