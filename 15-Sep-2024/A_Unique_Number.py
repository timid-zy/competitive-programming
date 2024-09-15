from collections import Counter

def solve():
    input()
    A = list(map(int, input().split()))
    counter = Counter(A)
    filtered = []
    for i in range(len(A)):
        if counter[A[i]] == 1:
            filtered.append((A[i], i+1))
    
    if len(filtered) == 0:
        return -1

    return min(filtered, key=lambda x: x[0])[1]


for _ in range(int(input())):
    print(solve())