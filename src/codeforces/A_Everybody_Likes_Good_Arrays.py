def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    p = arr[0]
    res = 0
    for i in range(1, len(arr)):
        if p%2 == arr[i]%2:
            p *= arr[i]
            res += 1
        else:
            p = arr[i]
    
    return res


for _ in range(int(input())):
    print(solve())