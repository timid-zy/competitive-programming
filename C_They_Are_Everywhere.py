from collections import Counter

input()
s = input()
counter = Counter(s)

curr = {}
found = 0
min_len = float('inf')
st = 0

for i in range(len(s)):
    if s[i] not in curr or curr[s[i]] == 0:
        found += 1
    curr[s[i]] = curr.get(s[i], 0) + 1

    while found == len(counter) and st < len(s):
        min_len = min(min_len, i - st + 1)
        curr[s[st]] -= 1
        if curr[s[st]] == 0:
            found -= 1
        
        st += 1
    
print(min_len)