from collections import Counter

def solve():
    N = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a3 = list(map(int, input().split()))

    counter1 = Counter(a1)
    counter2 = Counter(a2)
    counter3 = Counter(a3)

    for k in counter1:
        if counter1[k] != counter2[k]:
            print(k)
            break
    
    for k in counter2:
        if counter2[k] != counter3[k]:
            print(k)
            break
    
solve()
