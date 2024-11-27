def solve():
    n = int(input())
    if n < 4:
        return -1

    if n in [5, 7, 11]:
        return -1

    res = n // 4

    if n % 4 == 0 or n % 4 == 2:
        return res
    else:
        return res - 1


for _ in range(int(input())):
    print(solve())
