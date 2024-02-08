import math
n, k, q = list(map(int, input().split(" ")))

arr = [0] * 200002
min_num = 200001
max_num = 0

for i in range(n):
    l, r = list(map(int, input().split(" ")))
    min_num = min(min_num, l, r)
    max_num = max(max_num, l, r)
    arr[l] += 1
    arr[r+1] -= 1

for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]

for i in range(1, len(arr)):
    if arr[i] >= k:
        arr[i] = arr[i - 1] + 1
    else:
        arr[i] = arr[i - 1]

arr[max_num + 1] = 0

for i in range(q):
    l, r = list(map(int, input().split()))
    if l <= min_num and r >= max_num:
        print(arr[max_num])
    elif l <= min_num:
        print(arr[r])
    elif r >= max_num:
        print(arr[max_num] - arr[l - 1])
    else:
        print(arr[r] - arr[l-1])