n, k = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for n in A:
    strn = str(n)
    lc = 0
    for c in strn:
        if c == "4" or c == "7":
            lc += 1

    if lc <= k:
        count += 1

print(count)