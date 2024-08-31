for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    min_num = arr[0]
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_idx = i
            min_num = arr[i]
    

    prev = arr[min_idx]
    possible = True
    for i in range(min_idx, len(arr)):
        if arr[i] < prev:
            possible = False
            break
        prev = arr[i]
    
    if possible: print(min_idx)
    else: print(-1)