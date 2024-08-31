from collections import deque
n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

max_arr = [0] * len(arr)
max_arr[0] = arr[0]
for i in range(1, len(arr)):
    max_arr[i] = max(max_arr[i-1], arr[i])

deq = deque(arr)
for i in range(len(arr) - 1):
    A = deq.popleft()
    B = deq.popleft()
    if A > B:
        deq.append(B)
        deq.appendleft(A)
    else: 
        deq.append(A)
        deq.appendleft(B)

deq = list(deq)
max_el = deq[0]
deq = deq[1:]
max_arr = [0] + max_arr
for i in range(k):
    step = int(input())
    
    if step <= len(arr) - 1:
        print(max_arr[step], arr[step])
    else:
        step = step % (len(arr) - 1)
        print(max_el, deq[step - 1])