for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [0] * 51
    for __ in range(n):
        l, r = map(int, input().split())
        if not (l <= k and r >= k):
            continue

        arr[l-1] += -1
        arr[r] += 1
    
    for i in range(len(arr) - 2, -1, -1):
        arr[i] += arr[i+1]
    
    if (max(arr) == arr[k] and arr.count(arr[k]) == 1):
        print("YES")
    else:
        print("NO")