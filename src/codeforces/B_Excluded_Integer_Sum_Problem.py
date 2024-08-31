for _ in range(int(input())):
    N, K, X = map(int, input().split())
    if X != 1:
        print("YES")
        print(N)
        print("1 " * N)
        continue

    if N == 1: 
        print("NO")
        continue

    if K == 2:
        if N % 2 == 0:
            print("YES")
            print(N // 2)
            print("2 " * (N // 2))
        else:
            print("NO")

        continue
    
    if K >= 3:
        print("YES")
        if N % 3 == 0:
            print(N//3)
            print("3 " * (N // 3))
        elif N % 3 == 1:
            print(N//3  + 1)
            print(("3 " * (N // 3 - 1)) + "2 2")
        else:
            print(N//3  + 1)
            print(("3 " * (N // 3)) + "2")
        continue

    if K % 2 == X % 2:
        print("NO")
        continue

    print("YES")
    if K % 2 == 0:
        print(N // 2)
        print("2 " * (N // 2))
    else:
        print(N // 3)
        print("3 " * (N // 3))
