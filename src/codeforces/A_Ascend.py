input()
arr = list(map(int, input().split()))

ans = 1
curr = 1
prev = arr[0]

for i in range(1, len(arr)):
    if arr[i] > prev:
        curr += 1
    else:
        curr = 1
    
    ans = max(ans, curr)
    prev = arr[i]

print(ans)