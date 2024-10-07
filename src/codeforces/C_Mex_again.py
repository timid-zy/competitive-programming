N = int(input())
arr = list(map(int, input().split()))

c = 1
arr.sort()
for i in range(len(arr)):
    if c <= arr[i]:
        c += 1

print(c)