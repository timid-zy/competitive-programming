for _ in range(int(input())):
    N, K = map(int, input().split())
    s = ""
    for i in range(N):
        un = (i % K) + 97
        s += chr(un)
    
    print(s)