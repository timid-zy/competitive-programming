import math
for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    arr.sort()

    median = math.ceil(len(arr) / 2) - 1
    ans = 0
    for i in range(median, len(arr)):
        if arr[i] == arr[median]:
            ans += 1
    
    print(ans)