n, a, b = map(int, input().split())
res = (a + b) % n
if res == 0:
    res = n

print(res)