prefix = None
for _ in range(int(input())):
    s = input()
    if prefix is None:
        prefix = s
        continue

    i = j = 0
    while i < len(prefix) and j < len(s):
        if prefix[i] == s[j]:
            i += 1
            j += 1
        else:
            break
    
    prefix = prefix[:i]

print(len(prefix))