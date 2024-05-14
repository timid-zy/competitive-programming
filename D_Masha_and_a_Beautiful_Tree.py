def mergeSort(arr):
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    left, cl = mergeSort(arr[:mid])
    right, cr = mergeSort(arr[mid:])

    arr, new_c = merge(left, right)
    return arr, new_c + cl + cr

def merge(left, right):
    if left[0] > right[0]:
        return right + left, 1
    else:
        return left + right, 0


for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    new_arr, count = mergeSort(arr)

    is_sorted = True
    for i in range(1, len(new_arr)):
        if new_arr[i] < new_arr[i - 1]:
            is_sorted = False
            break

    if is_sorted: print(count)
    else: print(-1)
