for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    mx = max(arr)
    mn = min(arr)
    print(mx - mn)
    