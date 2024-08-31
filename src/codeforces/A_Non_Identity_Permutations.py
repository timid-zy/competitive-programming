for _ in range(int(input())):
    N = int(input())
    arr = list(range(N, 0, -1))
    if N % 2 == 1:
        arr[len(arr) // 2], arr[-1] = arr[-1], arr[len(arr) // 2]
    
    print(*arr)