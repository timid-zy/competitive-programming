for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    flag = True
    for i in range(1, len(arr) - 1):
        if arr[i - 1] == 0:
            continue
        
        ops = arr[i - 1]
        arr[i - 1] -= ops
        arr[i] -= ops * 2
        arr[i + 1] -= ops
        
        if arr[i] < 0 or arr[i + 1] < 0 or (arr[i] > 0 and arr[i + 1] == 0):
            flag = False
            break
    
    if flag and arr[-1] == 0 and arr[-2] == 0:
        print('YES')
    else:
        print('NO')