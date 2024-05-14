for i in range(int(input())):
    arr = list(map(int, input().split()))

    if arr[0] == 0 and sum(arr) != 0:
        print(1)
        continue
    
    ans = arr[0] + 2 * min(arr[1], arr[2]) + min(arr[0] + 1, arr[3] + abs(arr[1] - arr[2]))
    print(ans)