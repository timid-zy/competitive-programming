def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def solve():
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    gc = gcd(A, C)
    if abs(B-D) % gc != 0:
        print(-1)
        return

    rick = B
    morty = D
    while True:
        if rick == morty:
            print(rick)
            return
        
        if rick > morty:
            morty += C
        elif morty > rick:            
            rick += A

solve()