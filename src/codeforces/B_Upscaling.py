for _ in range(int(input())):

    n = int(input())
    c = ["##", ".."]
    curr = 0
    for i in range(n):
        s = ""
        i = curr
        for j in range(n):
            s += c[i]
            i = (i + 1) % 2
        
        print(s)
        print(s)
        curr = (curr + 1) % 2