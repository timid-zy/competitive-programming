"""
s1, s2 = input().lower(), input().lower()
ans = 1 if s1 > s2 else -1 if s1 < s2 else 0
print(ans)
"""

s1, s2 = input().lower(), input().lower()
ans = 0
for i in range(len(s1)):
    c1 = ord(s1[i])
    c2 = ord(s2[i])
    if c1 < 97: c1 += 32
    if c2 < 97: c2 += 32

    if c1 > c2:
        ans = 1
        break
    
    if c1 < c2:
        ans = -1
        break

print(ans)
