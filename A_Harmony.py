tests = int(input())
for i in range(tests):
    n, k = list(map(int, input().split()))

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr2.sort(reverse=True)

    flag = True
    for j in range(len(arr1)):
        if arr1[j] + arr2[j] > k:
            flag = False
            break
    
    if flag: print('Yes')
    else: print('No')
    if i < tests - 1:
        input()