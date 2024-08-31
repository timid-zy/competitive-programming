for _ in range(int(input())):
    v = int(input())
    if v == 1:
        print(2)
        continue

    elif v % 3 == 0:
        print(v // 3)
    
    else:
        print(v // 3 + 1)