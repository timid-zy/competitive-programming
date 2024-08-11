for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    dct = {arr[i]: i for i in range(len(arr))}
    consec = 0
    for n in range(2, N + 1):
        if dct[n] > dct[n-1]:
            consec += 1
    
    print(N - consec - 1)
