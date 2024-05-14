for i in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = input().split()
    
    set1 = set(arr[:len(arr) // 2])
    set2 = set(arr[len(arr) // 2:])
    nonunique = set1.intersection(set2)
    unique1 = set1 - set2
    unique2 = set2 - set1
    
    
    ans1 = []
    ans2 = []

    added = 0
    for item in unique1:
        if added == k * 2: break
        ans1.append(item)
        ans1.append(item)
        added += 2

    added = 0
    for item in unique2:
        if added == k * 2: break
        ans2.append(item)
        ans2.append(item)
        added += 2

    if added < k * 2:
        for item in nonunique:
            if added == k * 2:
                break
            ans1.append(item)
            ans2.append(item)
            added += 1
        
    
    
    print(" ".join(ans1))
    print(" ".join(ans2))