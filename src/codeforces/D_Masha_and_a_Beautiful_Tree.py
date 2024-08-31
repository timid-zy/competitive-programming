def mergeSort(arr):
    if len(arr) == 1: return arr, 0

    mid = len(arr) // 2
    left, cl = mergeSort(arr[:mid])
    right, cr = mergeSort(arr[mid:])

    ar, cn = merge(left, right)
    return ar, cn + cl + cr

def merge(left, right):
    if left[0] > right[0]:
        return right + left, 1
    else:
        return left + right, 0

for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    A, count = mergeSort(A)
    valid = True
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            valid = False
            break
    
    if valid: print(count)
    else: print(-1)