def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for i in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    mn = min(arr)
    mx = max(arr)
    if mn == mx:
        print(0)
        continue

    if k <= mx and k >= mn:
        print(-1)
        continue 
    
    curr = abs(arr[0] - k)
    for i in range(len(arr)):
        curr = gcd(curr, abs(arr[i] - k))
    
    count = 0
    for i in range(len(arr)):
        count += (abs(arr[i] - k) // curr)
    
    print(count - len(arr))