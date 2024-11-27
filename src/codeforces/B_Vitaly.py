from collections import Counter

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    zeroset = []
    pos = neg = None
    for n in arr:
        if n > 0 and pos is None:
            pos = n
        elif n < 0 and neg is None:
            neg = n
        else:
            zeroset.append(n)
    
    if pos is not None and neg is not None:
        print(1, neg)
        print(1, pos)
        print(len(zeroset), *zeroset)
        return
    
    n1 = n2 = None
    popped = []
    for i in range(len(zeroset)):
        if zeroset[i] < 0:
            if n1 is None:
                n1 = zeroset[i]
                popped.append(i)
            elif n2 is None:
                n2 = zeroset[i]
                popped.append(i)
            
        if n1 is not None and n2 is not None:
            break
    
    zeroset.pop(popped[1])
    zeroset.pop(popped[0])
    print(1, neg)
    print(2, n1, n2)
    print(len(zeroset), *zeroset)

solve()