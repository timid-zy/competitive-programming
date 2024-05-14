import bisect
input()
arr = list(map(int, input().split()))
arrows = list(map(int, input().split()))
prefix = [arr[0]]
for i in range(1, len(arr)): prefix.append(prefix[-1] + arr[i])

dmg = 0
for i in range(len(arrows)):
    dmg += arrows[i]
    if dmg >= prefix[-1]:
        print(len(arr))
        dmg = 0
        continue

    r = bisect.bisect_right(prefix, dmg) - 1
    print(len(arr) - r - 1)