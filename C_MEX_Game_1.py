from collections import Counter

for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    arr.sort()
    set1 = set(arr)
    counter = Counter(arr)

    found = None
    candidate = None
    for i in range(len(arr)):
        if counter[arr[i]] == 1:
            if found is None or found == arr[i]:
                found = arr[i]
                continue
            candidate = arr[i]
            break
    
    if candidate is None:
        candidate = arr[-1] + 1
    
    for i in range(candidate + 1):
        if i not in set1 or i == candidate:
            print(i)
            break