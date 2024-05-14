s = input()

prefix = [0] * len(s)
prefix[0] = 0
curr = s[0]
for i in range(1, len(s)):
    if s[i] == curr:
        prefix[i] = prefix[i - 1] + 1
    else:
        prefix[i] = prefix[i - 1]
    curr = s[i]

for i in range(int(input())):
    l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    if l == 0:
        print(prefix[r])
    else:
        print(prefix[r] - prefix[l])