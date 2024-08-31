import bisect
input()
arr = list(map(int, input().split()))
arr.sort()
s = ""
for i in range(int(input())):
    i, j = list(map(int, input().split()))
    l = bisect.bisect_left(arr, i)
    r = bisect.bisect_right(arr, j)
    s += str(r - l) + " "

print(s)