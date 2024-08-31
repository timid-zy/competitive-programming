for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    left_min = [(arr[0], 0)]
    curr_min = (arr[0], 0)
    for i in range(1, len(arr)):
        if curr_min[0] > arr[i]:
            curr_min = (arr[i], i)
        left_min.append(curr_min)

    right_min = [(arr[-1], len(arr) - 1)]
    curr_min = (arr[-1], len(arr) - 1)
    for i in range(len(arr) - 2, -1, -1):
        if curr_min[0] > arr[i]:
            curr_min = (arr[i], i)
        right_min.append(curr_min)
    right_min = right_min[::-1]
    
    ans = None
    for i in range(len(arr)):
        if left_min[i][0] < arr[i] and right_min[i][0] < arr[i]:
            ans = (left_min[i][1] + 1, i + 1, right_min[i][1] + 1)
    
    if ans:
        print('YES')
        print(ans[0], ans[1], ans[2])
    else:
        print('NO')