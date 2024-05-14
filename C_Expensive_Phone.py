for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    if len(arr) <= 0:
        print(0)
        continue
    
    min_num = arr[-1]
    count = 0
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > min_num:
            count += 1
        elif arr[i] < min_num:
            min_num = arr[i]
    
    print(count)