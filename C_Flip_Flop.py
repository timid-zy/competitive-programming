for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    curr_score = 0
    one_count = 0
    max_score = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            one_count += 1
        else:
            curr_score += one_count
    max_score = curr_score
    
    curr_score = 0
    one_count = 0
    first_zero = None
    if 0 in arr:
        first_zero = arr.index(0)
    if first_zero is not None:
        arr2 = arr[:]
        arr2[first_zero] = 1
        for i in range(len(arr2)):
            if arr2[i] == 1:
                one_count += 1
            else:
                curr_score += one_count   
        max_score = max(max_score, curr_score)

    curr_score = 0
    one_count = 0
    last_one = None
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 1:
            last_one = i
            break
    if last_one is not None:
        arr2 = arr[:]
        arr2[last_one] = 0
        for i in range(len(arr2)):
            if arr2[i] == 1:
                one_count += 1
            else:
                curr_score += one_count
        max_score = max(max_score, curr_score)
    
    print(max_score)