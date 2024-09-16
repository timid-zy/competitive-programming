from collections import Counter

def solve():
    S, T = input().split()
    counter = Counter(T)
    ti = len(T) - 1
    for i in range(len(S) - 1, -1, -1):
        if S[i] == T[ti]:
            counter[S[i]] -= 1
            ti -= 1
        
        elif counter[S[i]] > 0:
            break

        if ti == -1:
            break
    
    return "YES" if ti == -1 else "NO"

for _ in range(int(input())):
    print(solve())