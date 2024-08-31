for i in range(int(input())):
    n, k = list(map(int, input().split()))


    str1 = ["a"] * n
    inc = 0
    curr = 1
    while curr < k:
        inc += 1
        curr += inc
        # curr -= inc
    if inc == 0:
        str1[-1] = "b"
        str1[-2] = "b"
        print("".join(str1))
        continue
    elif inc == n - 1:
        str1[0] = "b"
    else:
        # print(inc, (-1 * inc - 2))
        str1[(-1 * inc - 2)] = "b"
    print(curr, inc, k)
    print("".join(str1))