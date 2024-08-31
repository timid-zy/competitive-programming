def heapify_down(arr, st):
    curr = st
    l, r = curr * 2 + 1, curr * 2 + 2
    child = r if r < len(arr) and arr[l] > arr[r] else l

    while l < len(arr) and arr[child] < arr[curr]:
        arr[child], arr[curr] = arr[curr], arr[child]

        curr = child
        l, r = curr * 2 + 1, curr * 2 + 2
        child = r if r < len(arr) and arr[l] > arr[r] else l

def heapify(arr):
    for i in range(len(arr) - 1, -1, -1):
        heapify_down(arr, i)
    

arr = [3,10,6,9,10,16,23,5,45,2,34,12,34,1]
heapify(arr)
print(arr)