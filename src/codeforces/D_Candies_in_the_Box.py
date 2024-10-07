def check_K(N, k):
    n = N
    vasya = 0
    while n > 0:
        vasya += min(k, n)
        n -= min(k, n)

        d = n // 10
        n -= d
    
    return vasya * 2 >= N

N = int(input())
l, r = 1, N
while l < r:
    mid = l + (r - l) // 2
    if check_K(N, mid):
        r = mid
    else:
        l = mid + 1

print(l)