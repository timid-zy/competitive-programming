n = int(input())
arr = list(map(int, input().split()))

mn = min(arr)
mx = max(arr)

print(mn + (mx - mn) // 2)