def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    if N == K:
        sum_ = 0
        for i in range(len(arr)): sum_ += (i + 1) * arr[i]
        return sum_ 

    suffix = [arr[-1]] * len(arr)
    for i in range(len(arr)-2, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]

    suffix.pop(0)
    suffix.sort()
    return sum(suffix[-(K-1):]) + sum(arr) if K > 1 else sum(arr)

print(solve())