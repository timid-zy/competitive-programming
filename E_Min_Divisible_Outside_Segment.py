def solve(l, r, d):
    if d == 1:
        if l == 1:
            return r + 1
        else:
            return 1

    c = d
    if not (l <= c <= r):
        return c

    if (l <= c <= r):
        return (r // d) * d + d


for _ in range(int(input())):
    l, r, d = map(int, input().split())
    print(solve(l,r,d))