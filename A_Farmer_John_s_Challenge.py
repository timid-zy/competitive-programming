for i in range(int(input())):
    n, k = map(int, input().split())

    if n == k:
        a = ["1"] * n
        s = " ".join(a)
        print(s)
    
    elif k == 1:
        a = ["1"] * (n - 1)
        a.append("2")
        s = " ".join(a)
        print(s)
    
    else:
        print(-1)
        
