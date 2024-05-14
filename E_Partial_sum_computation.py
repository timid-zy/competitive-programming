for i in range(int(input())):
    input()

    arr = list(map(int, input().split(" ")))

    arr.sort()
    
    if arr[0] != 1:
        print('NO')
        continue

    flag = True
    r_sum = 1
    for i in range(1, len(arr)):
        if r_sum < arr[i]:
            flag = False
            break
        r_sum += arr[i]
        

    if flag:
        print('YES')
    else:
        print('NO')
