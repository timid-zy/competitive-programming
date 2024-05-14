for i in range(int(input())):
    n, m, k = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()
    arr2.sort()
    
    j = len(arr2) - 1
    count = 0
    for i in range(len(arr1)):
        while j >= 0 and arr1[i] + arr2[j] > k:
            j -= 1
        
        if j == -1:
            break
            
        count += j + 1
    
    print(count)