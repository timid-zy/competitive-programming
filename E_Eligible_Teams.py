for i in range(int(input())):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    curr_min = float('inf')
    curr_len = 0
    count = 0

    for i in range(len(arr)):
        curr_min = min(curr_min, arr[i])
        curr_len += 1

        if (curr_min * curr_len) >= x:
            curr_min = float('inf')
            curr_len = 0
            count += 1
    
    print(count)