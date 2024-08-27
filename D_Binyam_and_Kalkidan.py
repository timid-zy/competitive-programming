def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

def find_rep(c, arr):
    c = int(c)
    v = factorial(c)
    for i in [7, 5, 3, 2]:
        d = factorial(i)
        while v % d == 0:
            arr.append(i)
            v //= d

input()
s = input()
s = s.replace("0", "").replace("1", "")

arr = []
for c in s:
    find_rep(c, arr)
arr.sort(reverse=True)

print("".join(map(str, arr)))