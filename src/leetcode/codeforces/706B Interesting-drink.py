import bisect

input()
arr = list(map(int, input().split()))
arr.sort()

for i in range(int(input())):
    print(bisect.bisect_right(arr, int(input())))