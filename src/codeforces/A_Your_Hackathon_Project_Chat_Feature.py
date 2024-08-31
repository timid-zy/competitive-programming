for _ in range(int(input())):
    input()
    s = input()
    c = 0
    stop = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ")":
            stop = i
            break
        
        c += 1
    
    ans = "Yes" if c > stop + 1 else "No"
    print(ans)