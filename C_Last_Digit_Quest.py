for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    dict1 = {}

    found = False
    for i in range(len(arr)):
        last_digit = arr[i] % 10
        
        
        for i in range(10):
            if i not in dict1: continue
            for j in range(10):
                if j not in dict1: continue
                if i == j and dict1[i] == 1: continue
                if (i + j + last_digit) % 10 == 3:
                    found = True
                    break
            
        dict1[last_digit] = dict1.get(last_digit, 0) + 1
    
    if found:
        print('YES')
    else:
        print('NO')