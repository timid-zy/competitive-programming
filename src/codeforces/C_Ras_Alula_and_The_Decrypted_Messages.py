for i in range(int(input())):
    n, k = list(map(int, input().split()))
    s1 = input()
    s2 = input()

    offset = 0
    for i in range(k):
        ops = ord(s1[i]) - ord(s2[i])
        offset += ops
    
    found = False
    for st in range(1, len(s1) - k + 1):
        if offset == 0:
            found = True
            break
            
        offset -= ord(s1[st - 1])
        offset += ord(s1[st + k - 1])


    if offset == 0:
        found = True
    
    if found:
        print('YES')
    else:
        print('NO')