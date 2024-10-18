def solve():
    S = input()
    res = (ord(S[0]) - ord('a')) * 25 + (ord(S[1]) - ord('a'))
    if S[0] > S[1]:
        res += 1
    
    return res


for _ in range(int(input())):
    print(solve())