s = input()
counter = [0] * 26
for c in s: 
    counter[ord(c) - ord('a')] += 1

mc = 0
u = []
t = []
for i in range(len(s)):
    while counter[mc] == 0:
        mc += 1
    
    while t and ord(t[-1]) - ord('a') <= mc:
        u.append(t.pop())

    cid = ord(s[i]) - ord('a')
    if cid == mc:
        u.append(s[i])
    else:
        t.append(s[i])
    
    counter[cid] -= 1

print("".join(u + t[::-1]))