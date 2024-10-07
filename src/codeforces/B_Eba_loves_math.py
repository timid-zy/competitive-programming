for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    ans = A[0]
    for n in A: ans &= n

    print(ans)