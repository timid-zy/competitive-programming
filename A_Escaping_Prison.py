for i in range(int(input())):
    n, k = list(map(int, input().split()))
    sum_ = 0
    for i in range(n):
        sum_ += max(list(map(int, input().split())))
    
    if sum_ >= k:
        print('YES')
    else:
        print('NO')