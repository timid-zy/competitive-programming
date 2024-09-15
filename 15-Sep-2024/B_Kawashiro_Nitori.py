def solve():
    N, K = map(int, input().split())
    S = input()
    if K == 0:
        return "YES"

    if len(S) < (K*2 + 1):
        return "NO"
    
    i, j = 0, len(S)-1
    while i < j:
        if i == K:
            return "YES"

        if S[i] != S[j]:
            return "NO"

        i += 1
        j -= 1
    
    return "YES"

for _ in range(int(input())):
    print(solve())
