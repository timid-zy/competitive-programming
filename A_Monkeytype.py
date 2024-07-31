for _ in range(int(input())):
    keys = input()
    pos = {}
    for i in range(len(keys)):
        pos[keys[i]] = i
    
    st = input()
    c = pos[st[0]]
    res = 0
    for i in range(1, len(st)):
        res += abs(c - pos[st[i]])
        c = pos[st[i]]
    
    print(res)