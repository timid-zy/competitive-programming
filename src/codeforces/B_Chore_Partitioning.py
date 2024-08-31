N, A, B = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

print(arr[-A] - arr[B-1])