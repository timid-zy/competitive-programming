import math

def get_score(a,  b, c1, c2, A):
    
    temp = abs(a-b) % A
    if temp - c1 >= 0:
        temp = min(temp, temp - c1)
    if temp - c2 >= 0:
        temp = min(temp, temp - c2)
    
    temp = min(temp, abs(b-(a+A)))
    print(a, b, temp)
    return temp

def solve():
    N, A, B = map(int, input().split())
    ARR = list(map(int, input().split()))
    if A > B:
        A, B = B, A

    c1 = B - ((B // A) * A)
    c2 = (math.ceil(B / A) * A) - B
    print(c1, c2)
    L, R = ARR[0], ARR[1]
    score = get_score(L, R, c1, c2, A)
    for i in range(2, len(ARR)):
        if get_score(L, ARR[i], c1, c2, A) > get_score(R, ARR[i], c1, c2, A) > score:
            score = get_score(L, ARR[i], c1, c2, A)
            R = ARR[i]
        elif get_score(R, ARR[i], c1, c2, A) > score:
            score = get_score(R, ARR[i], c1, c2, A)
            L = ARR[i]
    
    return score

for _ in range(int(input())):
    print(solve())