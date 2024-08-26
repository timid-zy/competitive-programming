N, K = list(map(int, input().split()))
s = input().lower()

arr = [0] * K
for i in range(len(s)):
    c = ord(s[i]) - 97
    if c < len(arr):
        arr[c] += 1

print(min(arr) * len(arr))