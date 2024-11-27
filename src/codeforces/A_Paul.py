from collections import Counter

for _ in range(int(input())):
    s = input()
    counter = Counter(s)
    res = 0
    for k in counter:
        res += min(2, counter[k])
    
    print(res//2)