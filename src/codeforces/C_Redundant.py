from collections import defaultdict

s = input()
dct = defaultdict(int)
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        dct[s[i:j]] += 1

res = 0
for k in dct:
    if dct[k] > 1 and res < len(k):
        res = len(k)

print(res)