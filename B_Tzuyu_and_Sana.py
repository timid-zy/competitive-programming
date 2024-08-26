for _ in range(int(input())):
    a, b = map(int, input().split())
    A, B = bin(a)[2:], bin(b)[2:]
    A = ((32 - len(A)) * "0") + A
    B = ((32 - len(B)) * "0") + B
    x = ["0"] * 32
    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == "1":
                x[i] = "1"
    x = int("".join(x), 2)
    print((int(A, 2) ^ x) + (int(B, 2) ^ x))
