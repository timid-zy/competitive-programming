from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    counter = defaultdict(int)
    for c in arr:
        counter[abs(c)] += 1
    
    res = 0
    for k in counter:
        if k == 0:
            res += 1
        else:
            res += min(counter[k], 2)
    
    return res


for _ in range(int(input())):
    print(solve())