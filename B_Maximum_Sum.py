for i in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    r_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        r_sum += arr[i]
        max_sum = max(max_sum, r_sum)
        if r_sum < 0:
            r_sum = 0
    
    mod = pow(10, 9) + 7
    ans = sum(arr)
    for i in range(k):
        ans = (ans + max_sum) % mod
        max_sum = (max_sum + max_sum) % mod
    
    print(ans % mod)