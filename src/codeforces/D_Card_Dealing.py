for _ in range(int(input())):
    N = int(input()) - 1
    al, bo = 1, 0
    isal = False
    curr = 2
    while N > 0:
        add = min(curr, N)
        if isal:
            al += add
        else:
            bo += add
        
        N -= add
        curr += 1
        if N == 0: break

        add = min(curr, N)
        if isal:
            al += add
        else:
            bo += add
        
        N -= add
        if N == 0: break
        curr += 1
        isal = not isal
    
    print(al, bo)