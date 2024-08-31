for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    excess = 0
    to_transfer = 0
    steps = 0
    for i in range(len(arr) - 1):
        if arr[i] == 0 and to_transfer == 0:
            continue
            
        to_transfer += arr[i]
        excess += arr[i] - 1
        if arr[i] == 0:
            steps += 1
            
    
    print(steps + to_transfer)
