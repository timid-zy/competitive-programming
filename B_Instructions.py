for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    memo = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        memo[i] = arr[i]
        if i + arr[i] < len(arr):
            memo[i] += memo[i + arr[i]]
    
    print(max(memo))