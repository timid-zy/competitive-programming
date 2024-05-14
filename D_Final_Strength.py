def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    # count
    l = [0] * len(left)
    r = [0] * len(right)
    p = 0
    for i in range(len(left)):
        while p < len(right) and right[p][0] < left[i][0]:
            p += 1
        
        l[i] = p
    
    
    p = 0
    for i in range(len(right)):
        while p < len(left) and left[p][0] < right[i][0]:
            p += 1
        
        r[i] = p
    
    
    for i in range(len(left)):
        left[i] = (left[i][0] + l[i], left[i][1])
        
    for i in range(len(right)):
        right[i] = (right[i][0] + r[i], right[i][1])
    

    # merge
    ans = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l][0] < right[r][0]:
            ans.append(left[l])
            l += 1
        else:
            ans.append(right[r])
            r += 1
    
    ans.extend(left[l:])
    ans.extend(right[r:])

    return ans


for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    count = 0
    ret = mergeSort(list(zip(arr, range(len(arr)))))
    ans = [0] * len(arr)

    for val, pos in ret:
        ans[pos] = str(val)
    
    print(" ".join(ans))