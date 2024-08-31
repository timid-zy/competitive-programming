def factorial(x):
    if x <= 1:
        return 1

    return x * factorial(x-1)

N = int(input())
A = list(map(int, input().split()))
C = len(set(A))
print(factorial(C))