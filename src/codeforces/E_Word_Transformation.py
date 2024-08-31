from collections import Counter

for _ in range(int(input())):
    S, T = input().split()
    counter = Counter(T)
    j = len(T) - 1
    ans = False
    for i in range(len(S) - 1, -1, -1):
        if S[i] == T[j]:
            counter[S[i]] -= 1
            j -= 1
        
        elif counter[S[i]] > 0:
            break
        
        if j == -1:
            ans = True
            break
    
    ans = "YES" if j == -1 else "NO"
    print(ans)