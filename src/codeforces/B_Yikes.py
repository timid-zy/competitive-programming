import bisect
input()
arr = list(map(int, input().split()))
input()
queries = list(map(int, input().split()))
prefix = [arr[0]]

for i in range(1, len(arr)):
    prefix.append(prefix[-1] + arr[i])

for i in range(len(queries)):
    print(bisect.bisect_left(prefix, queries[i]) + 1)