n, m = map(int, input().split())
valid = True
prev = ""

for i in range(n):
    if not valid:
        break
    s = input()

    for j in range(len(s) - 1):
        if s[j] == prev:
            valid = False
        if s[j] != s[j + 1]:
            valid = False
    
        if not valid:
            break
    
    prev = s[0]

if valid:
    print('YES')
else:
    print('NO')

