input()
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for i in range(len(queries)):
    target = queries[i]
    l, r = 0, len(queries)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] <= target:
            l = mid
        else:
            r = mid
    
    # if l == len(queries) - 1 and target > arr[l]: l += 1
    print(l)