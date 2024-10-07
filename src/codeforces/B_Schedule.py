def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N - 1, -1, -1):
        if arr[i] == 0:
            arr.pop()
        else:
            break

    arr = arr[::-1]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            arr.pop()
        else:
            break

    arr = arr[::-1]
    if len(arr) == 0:
        return 0

    c = i = 0
    while i < len(arr):
        if arr[i] == 1:
            c += 1
            i += 1
            continue
        
        zeroes = 0
        while i < len(arr) and arr[i] == 0:
            zeroes += 1
            i += 1
        
        if zeroes == 1:
            c += 1
    
    return c

print(solve())