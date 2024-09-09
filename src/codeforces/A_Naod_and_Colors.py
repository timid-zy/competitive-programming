from collections import Counter

def solve():
    int(input())
    A = list(map(int, input().split()))
    counter = Counter(A)
    return max(counter.values())


for _ in range(int(input())):
    print(solve())