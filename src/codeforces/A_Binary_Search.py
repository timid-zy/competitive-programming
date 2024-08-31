input()
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for i in range(len(queries)):
    target = queries[i]
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] >= target:
            r = mid
        else:
            l = mid + 1
    
    if arr[l] == target:
        print('YES')
    else:
        print('NO')