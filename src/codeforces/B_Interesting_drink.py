from bisect import bisect_right

input()
A = list(map(int, input().split()))
A.sort()
for _ in range(int(input())):
    n = int(input())
    print(bisect_right(A, n))