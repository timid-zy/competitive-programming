from collections import Counter

for _ in range(int(input())):
    input()
    s = input()
    counter = Counter(s)
    arr = ["b", "u", "g", "y", "r", "t"]
    res = ""
    for c in arr:
        res += (c * counter[c])
        counter[c] = 0
    
    for k in counter:
        res += (k * counter[k])
    
    print(res)
    