def check(val, arr):
    c = 0
    prev = float('-inf')
    for v in arr:
        if abs(v - prev) > val:
            c += 1
            prev = v + val

    return c <= 3


for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    A.sort()

    l, r = 0, max(A)
    while l < r:
        mid = l + (r - l) // 2
        if check(mid, A):
            r = mid
        else:
            l = mid + 1

    print(l)