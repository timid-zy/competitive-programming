for i in range(int(input())):
    input()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    count = 1
    prev = arr1[0]
    dict1 = {}
    for i in range(1, len(arr1)):
        if arr1[i] == prev:
            count += 1
        else:
            dict1[prev] = max(count, dict1.get(prev, 0))
            count = 1
            prev = arr1[i]
    dict1[prev] = max(count, dict1.get(prev, 0))


    count = 1
    prev = arr2[0]
    dict2 = {}
    for i in range(1, len(arr2)):
        if arr2[i] == prev:
            count += 1
        else:
            dict2[prev] = max(count, dict2.get(prev, 0))
            count = 1
            prev = arr2[i]
    dict2[prev] = max(count, dict2.get(prev, 0))
    
    mx = 0
    for key in dict1:
        mx = max(mx, dict1[key] + dict2.get(key, 0))
    for key in dict2:
        mx = max(mx, dict2[key] + dict1.get(key, 0))

    print(mx)

        