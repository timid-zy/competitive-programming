for i in range(int(input())):
    n, d = list(map(int, input().split()))
    s = input()

    flag = True
    for i in range(len(s)):
        if int(s[i]) < d:
            print(s[:i] + str(d) + s[i:])
            flag = False
            break
    
    if flag:
        print(s + str(d))